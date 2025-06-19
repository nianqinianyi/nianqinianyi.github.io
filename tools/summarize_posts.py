import os
import re
import requests
from glob import glob

POSTS_DIR = '../posts/'

    # Ollama API配置
OLLAMA_URL = "http://10.88.69.69:11434/api/chat"
MODEL_NAME = "qwen3:14b"

def generate_summary(content):
    try:
        # 构建请求数据
        payload = {
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": "请用一句话总结以下文章内容。"},
                {"role": "user", "content": content}  # 限制输入长度
            ],
            "stream": False
        }
        
        # 发送请求到本地Ollama
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=30
        )
        response.raise_for_status()  # 检查HTTP错误
        
        # 解析响应
        result = response.json()
        cleaned_content = re.sub(r"<think>.*?</think>\n?", "", result["message"]["content"], flags=re.DOTALL)
        return cleaned_content.strip()
        
    except requests.exceptions.ConnectionError:
        print("Error: 无法连接到Ollama服务，请确保Ollama已启动。")
    except requests.exceptions.Timeout:
        print("Error: 请求Ollama超时。")
    except Exception as e:
        print(f"Error generating summary with Ollama: {e}")
    
    # 回退到原始摘要方法
    sentences = [s.strip() for s in content.split('. ') if s.strip()]
    return sentences[0] + '.' if sentences else 'No content available.'

# 获取所有Markdown文件
md_files = glob(os.path.join(POSTS_DIR, '**/*.md'), recursive=True)

index = 0
for file_path in md_files:
    index += 1
    print(f"Processing file {index}/{len(md_files)}: {file_path}")
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 分离Front Matter和正文
        match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        if not match:
            print(f'No front matter found in {file_path}, skipping.')
            continue
        
        front_matter = match.group(1)
        body = match.group(2).strip()
        
        # 生成摘要
        summary = generate_summary(body)
        
        # 处理Front Matter行
        lines = front_matter.split('\n')
        # 匹配articleGPT和description字段的正则表达式，支持可选引号和任意缩进
        # pattern = re.compile(r'^(\s*)(articleGPT):\s*(["\']?)(.*?)\3\s*$')
        pattern = re.compile(r'^(\s*)(description):\s*(["\']?)(.*?)\3\s*$')
        new_lines = []
        for line in lines:
            m = pattern.match(line)
            if m:
                indent = m.group(1)  # 保留原始缩进
                key = m.group(2)
                quote = m.group(3) if m.group(3) else ''  # 保留原始引号格式
                # 替换值为摘要，保持原有引号格式
                new_line = f'{indent}{key}: {quote}{summary}{quote}'
                new_lines.append(new_line)
            else:
                new_lines.append(line)  # 非目标字段保持不变
        
        # 重建Front Matter
        new_front_matter = '\n'.join(new_lines)
        # 重建完整文件内容
        new_content = f'---\n{new_front_matter}\n---\n{body}\n'
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Processed: {file_path}')
    except Exception as e:
        print(f'Error processing {file_path}: {str(e)}')

print(f'Total processed files: {len(md_files)}')