import xml.etree.ElementTree as ET
import html2text
import os
import re
from datetime import datetime,timedelta

# 检查是否安装了html2text
try:
    import html2text
except ImportError:
    print("请先安装html2text: pip3 install html2text")
    exit(1)

# 配置文件路径
XML_FILE_PATH = "/Users/panic/workspace/data/WordPress.2022-12-21.xml"
TEMPLATE_FILE_PATH = "template.md"
TARGET_DIR = "target1"

# 创建目标目录
if not os.path.exists(TARGET_DIR):
    os.makedirs(TARGET_DIR)

# 定义XML命名空间
NAMESPACES = {
    'wp': 'http://wordpress.org/export/1.2/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
    'dc': 'http://purl.org/dc/elements/1.1/'
}

# 读取模板内容
try:
    with open(TEMPLATE_FILE_PATH, 'r', encoding='utf-8') as f:
        template_content = f.read()
    # 提取模板中的Front Matter部分
    template_front_matter = template_content.split('---')[1].strip()
except FileNotFoundError:
    print(f"模板文件 {TEMPLATE_FILE_PATH} 未找到")
    exit(1)
except IndexError:
    print(f"模板文件 {TEMPLATE_FILE_PATH} 格式不正确，缺少---分隔符")
    exit(1)

print("解析XML文件")
# 解析XML文件
try:
    # 尝试以UTF-8编码打开文件，处理可能的BOM头
    with open(XML_FILE_PATH, 'r', encoding='utf-8-sig') as f:
        content = f.read()
        
        # 使用正则表达式查找可能的</rss>结束标签（忽略大小写和周围空白）
        match = re.search(r'</\s*rss\s*>', content, re.IGNORECASE)
        if not match:
            print(f"警告: XML文件 {XML_FILE_PATH} 未找到有效的</rss>结束标签，尝试使用整个文件内容进行解析...")
            valid_content = content
        else:
            # 只保留到结束标签的有效内容
            valid_content = content[:match.end()]
        
        try:
            # 尝试使用lxml的容错解析器
            print("尝试使用lxml的容错解析器")
            from lxml import etree as ET
            parser = ET.XMLParser(recover=True, encoding='utf-8')
            root = ET.fromstring(valid_content.encode('utf-8'), parser=parser)
        except ImportError:
            # 回退到标准库解析器
            import xml.etree.ElementTree as ET
            try:
                root = ET.fromstring(valid_content)
            except ET.ParseError as e:
                print(f"XML文件 {XML_FILE_PATH} 解析错误: {e.msg} (行号: {e.lineno}, 位置: {e.position})")
                print("提示: 安装lxml可提高容错能力: pip3 install lxml")
                exit(1)
        except ET.ParseError as e:
            print(f"XML文件 {XML_FILE_PATH} 解析错误: {e.msg}")
            exit(1)
except UnicodeDecodeError:
    print(f"XML文件 {XML_FILE_PATH} 编码错误，无法用UTF-8解码")
    exit(1)
except FileNotFoundError:
    print(f"XML文件 {XML_FILE_PATH} 未找到")
    exit(1)

# 获取所有文章项
items = root.findall('./channel/item', namespaces=NAMESPACES)
print(f"items:{len(items)}")
# 配置HTML转Markdown
h = html2text.HTML2Text()
h.ignore_links = False
h.ignore_images = False

def extract_categories_and_tags(item):
    """提取文章的分类和标签"""
    categories = []
    tags = []
    # 查找所有分类和标签
    category_elements = item.findall('category', namespaces=NAMESPACES)
    for elem in category_elements:
        domain = elem.get('domain')
        print(f"domain:{domain}")
        if domain == 'category':
            categories.append(elem.text.strip())
        elif domain == 'post_tag':
            tags.append(elem.text.strip())
    return categories, tags

def convert_date(date_str):
    """将WordPress日期格式转换为YYYY-MM-DD HH:mm:ss"""
    try:
        # 解析输入的UTC时间字符串
        utc_datetime = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")
        # 转换为北京时间（UTC+8）
        beijing_datetime = utc_datetime + timedelta(hours=8)
        return beijing_datetime.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return '2023-01-01 00:00:00'  # 默认日期

def convert_date1(date_str):
    """将WordPress日期格式转换为YYYY-MM-DD HH:mm:ss"""
    try:
        # 解析输入的UTC时间字符串
        utc_datetime = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")
        # 转换为北京时间（UTC+8）
        beijing_datetime = utc_datetime + timedelta(hours=8)
        return beijing_datetime.strftime('%Y-%m-%d')
    except ValueError:
        return '2023-01-01'  # 默认日期

def generate_front_matter(title, categories, tags, date, description):
    """生成Markdown的Front Matter"""
    # 处理空值情况
    title = title or "无标题"
    description = description or title
    
    # 构建分类和标签字符串
    categories_str = ', '.join([f'"{c}"' for c in categories]) if categories else ''
    tags_str = ', '.join([f'"{t}"' for t in tags]) if tags else ''
    
    # 构建Front Matter
    front_matter = f"title: {title}\n"
    front_matter += f"tags: [{tags_str}]\n"
    front_matter += f"categories: [{categories_str}]\n"
    front_matter += f"date: {date}\n"
    front_matter += f"description: {description}\n"
    front_matter += "articleGPT: "  # 保留模板中的这个字段
    return front_matter

# 处理每个文章
for item in items:
    print("------------------")
    # 只处理文章类型，跳过页面等其他类型
    post_type = item.find('wp:post_type', namespaces=NAMESPACES)
    if post_type is None or post_type.text != 'post':
        continue
    
    # 提取文章基本信息
    # 安全获取元素内容，防止缺失元素导致错误
    title_elem = item.find('title', namespaces=NAMESPACES)
    title = title_elem.text.strip() if (title_elem is not None and title_elem.text) else "无标题"
    print(f"title:{title}")
    
    slug_elem = item.find('wp:post_name', namespaces=NAMESPACES)
    slug = slug_elem.text.strip() if (slug_elem is not None and slug_elem.text) else None
    
    pub_date_elem = item.find('pubDate', namespaces=NAMESPACES)
    pub_date = pub_date_elem.text if (pub_date_elem is not None and pub_date_elem.text) else datetime.now().isoformat()
    
    content_elem = item.find('content:encoded', namespaces=NAMESPACES)
    content_html = content_elem.text.strip() if (content_elem is not None and content_elem.text) else ''
    
    desc_elem = item.find('description', namespaces=NAMESPACES)
    description = desc_elem.text.strip() if (desc_elem is not None and desc_elem.text) else title
    
    # 处理slug为空的情况
    if not slug and title:
        slug = title.replace(' ', '-').lower()
    elif not slug:
        slug = f"post-{datetime.now().timestamp()}"
    
    # 提取分类和标签
    categories, tags = extract_categories_and_tags(item)
    
    # 转换日期格式
    date_str1 = convert_date1(pub_date)
    date_str = convert_date(pub_date)
    
    # 转换HTML内容为Markdown
    content_md = h.handle(content_html)
    
    # 生成Front Matter
    front_matter = generate_front_matter(title, categories, tags, date_str, description)
    
    # 组合完整的Markdown内容
    md_content = f"---\n{front_matter}\n---\n\n{content_md}"
    
    # 写入文件
    file_path = os.path.join(TARGET_DIR, f"{date_str1}-{slug}.md")
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"生成文件: {file_path}")
    except Exception as e:
        print(f"写入文件 {file_path} 失败: {str(e)}")

print("所有文章处理完成!")