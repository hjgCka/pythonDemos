from pathlib import Path

# 支持相对路径和绝对路径，text_files/user.txt
# /home/eric/data_files/text_files/user.txt
path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

if  "12" in pi_string:
    print("12 in the pi string")
else:
    print("12 not in the pi string")