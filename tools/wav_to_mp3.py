import argparse
import os
import sys

# 检查pydub是否安装
try:
    from pydub import AudioSegment
except ImportError:
    print("错误: 未找到pydub库，请先安装: pip install pydub")
    sys.exit(1)

def convert_wav_to_mp3(wav_path, article_path):
    """
    将WAV文件转换为MP3格式
    :param wav_path: WAV文件路径
    :return: 转换后的MP3文件路径，若失败则返回None
    """
    # 检查文件是否存在
    if not os.path.exists(wav_path):
        print(f"错误: 文件不存在 - {wav_path}")
        return None

    # 检查文件扩展名是否为wav
    if not wav_path.lower().endswith('.wav'):
        print(f"错误: {wav_path} 不是WAV文件")
        return None

    # 构建输出MP3文件路径
    mp3_path = article_path.replace('.md', '.mp3').replace('posts/', 'public/audios/')
    os.makedirs(os.path.dirname(mp3_path), exist_ok=True)

    try:
        # 加载WAV文件
        audio = AudioSegment.from_wav(wav_path)

        # 导出为MP3 (默认比特率128kbps)
        audio.export(mp3_path, format='mp3', bitrate='128k')
        print(f"转换成功: {mp3_path}")
        return mp3_path
    except Exception as e:
        print(f"转换失败: {str(e)}")
        print("提示: 确保已安装ffmpeg并添加到系统PATH中")
        return None

if __name__ == '__main__':
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='将WAV音频文件转换为MP3格式')
    parser.add_argument('wav_path', nargs='?', help='WAV文件路径')
    parser.add_argument('article_path', nargs='?', help='文件路径')

    # 解析命令行参数
    args = parser.parse_args()

    # 如果未提供文件路径，则提示用户输入
    if args.wav_path is None:
        args.wav_path = input("请输入WAV文件路径: ").strip()
        
    if args.article_path is None:
        args.article_path = input("请输入MD文件路径: ").strip()

    # 执行转换
    convert_wav_to_mp3(args.wav_path, args.article_path)