from pathlib import Path

path = Path('alice.txt')
#如果系统的默认编码与要读取的文件的编码不一致，参数encoding必不可少
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"File {path} not found")