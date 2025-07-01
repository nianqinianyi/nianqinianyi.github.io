import os
import re
import frontmatter
import markdown
from playwright.sync_api import sync_playwright

def md_to_pdf():
    # 获取用户输入的Markdown文件路径
    md_path = input("请输入Markdown文件路径: ").strip()
    
    # 检查文件是否存在
    if not os.path.exists(md_path):
        print(f"错误: 文件 '{md_path}' 不存在。")
        return
    
    # 检查文件是否为.md文件
    if not md_path.endswith('.md'):
        print("错误: 请输入有效的Markdown文件路径（以.md结尾）。")
        return
        
    # 获取tools文件夹路径
    tools_dir = os.path.dirname(os.path.abspath(__file__))
    # 提取文件名（不包含扩展名）
    md_filename = os.path.basename(md_path)
    pdf_filename = os.path.splitext(md_filename)[0] + '.pdf'
    pdf_path = os.path.join(tools_dir, pdf_filename)
    
    try:
        # 读取Markdown文件内容
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # 解析Front Matter
        try:
            post = frontmatter.loads(md_content)
        except frontmatter.exceptions.ParserError:
            print(f"错误: 无法解析文件 {md_path} 的Front Matter。")
            return
        
        # 检查是否存在标题
        if 'title' not in post.keys():
            print(f"错误: 文件 {md_path} 的Front Matter中缺少 'title' 字段。")
            return

        body = f"《{post.metadata['title']}》\n------\n\n{post.content}"
        
        # 将Markdown转换为HTML
        html_content = markdown.markdown(body, extensions=['fenced_code', 'codehilite'])
        
        # 添加基础CSS样式确保中文显示正常
        css_style = '''
        <style>
        body { font-family: 'SimHei', sans-serif; line-height: 1.6; padding: 20px; }
        .codehilite { background: #f8f8f8; padding: 15px; border-radius: 5px; overflow-x: auto; }
        pre { font-family: 'Consolas', 'Monaco', monospace; font-size: 14px; line-height: 1.4; }
        code { background: #f0f0f0; padding: 2px 4px; border-radius: 3px; }
        </style>
        '''
        html_content = f"<html><head><meta charset='UTF-8'>{css_style}</head><body>{html_content}</body></html>"
        
        # 将 html_content 写入一个 html文件中
        with open("test.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        
        # 使用Playwright通过无头浏览器生成PDF
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.set_content(html_content)
            page.pdf(
                path=pdf_path,
                format='A4',
                margin={"top": "20px", "right": "20px", "bottom": "20px", "left": "20px"}
            )
            browser.close()
        
        print(f"转换成功！PDF文件已保存至: {pdf_path}")
    except Exception as e:
        print(f"转换失败: {str(e)}")
        print("提示: 请确保已安装markdown和playwright库及浏览器。")
        print("安装命令:")
        print("  pip install markdown playwright pygments")
        print("  playwright install chromium")
    finally:
        pass

if __name__ == "__main__":
    # 调用终端运行命令，并输出
    os.system("pip -V")
    print(os.getcwd())
    md_to_pdf()