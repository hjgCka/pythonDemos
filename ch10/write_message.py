from pathlib import Path

# 会自动创建文件。python只能写入字符串，数值数据写入需要用str转换为字符串。
contents = "I love Python\n"
contents += "I love creating new games\n"
contents += "I also love working with data\n"
path = Path('programming.txt')
path.write_text(contents)