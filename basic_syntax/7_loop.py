current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

unconfirmed_users = ['alice', 'brian', 'candace']
# 一直运行，知道变为空
while unconfirmed_users:
    print(unconfirmed_users.pop())

pets = ['dog', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    # 一次只删除一个，循环遍历，多次执行
    pets.remove('cat')
print(pets)