import re
import sys
import requests

file_path = '../posts/2017/0627/spring-cloud-03.md'

# Ollama API配置
OLLAMA_URL = "http://10.88.69.69:11434/api/chat"
MODEL_NAME = "qwen3:14b"


def generate_summary(content, tag):
    print(f"generate summary for {tag}")

    system_content = "请以作者角度出发，一句话描述文章重点，不要出现第一人称" if tag == "description" else "请简单总结一下文章内容，不要出现换行等特殊内容。"

    try:
        # 构建请求数据
        payload = {
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": system_content},
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
        cleaned_content = re.sub(
            r"<think>.*?</think>\n?", "", result["message"]["content"], flags=re.DOTALL)
        return cleaned_content.strip()

    except requests.exceptions.ConnectionError:
        print("Error: 无法连接到Ollama服务，请确保Ollama已启动。")
    except requests.exceptions.Timeout:
        print("Error: 请求Ollama超时。")
    except Exception as e:
        print(f"Error generating summary with Ollama: {e}")

    sys.exit(1)


def replace_summary(content, front_matter, tag):
    # 生成摘要
    summary = generate_summary(content, tag)
    print(f"summary for {tag} is {summary}")

    # 处理Front Matter行
    lines = front_matter.split('\n')
    # 匹配articleGPT和description字段的正则表达式，支持可选引号和任意缩进
    pattern = re.compile(r'^(\s*)(description):\s*(["\']?)(.*?)\3\s*$') if tag == "description" else re.compile(
        r'^(\s*)(articleGPT):\s*(["\']?)(.*?)\3\s*$')
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

    return new_front_matter


def main():
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 分离Front Matter和正文
        match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        if not match:
            print(f'No front matter found in {file_path}, skipping.')
            sys.exit(1)

        front_matter = match.group(1)
        body = match.group(2).strip()

        # 生成并替换摘要
        front_matter = replace_summary(body, front_matter, "description")

        # 生成并替换摘要
        front_matter = replace_summary(body, front_matter, "articleGPT")

        # 重建完整文件内容
        new_content = f'---\n{front_matter}\n---\n{body}\n'

        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

    except Exception as e:
        print(f'Error processing {file_path}: {str(e)}')


if __name__ == '__main__':
    main()
