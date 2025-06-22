# 不会打印5 [,)
for value in range(1, 5):
    print(value)

for value in range(6):
    print(value)

for value in range(1, 50, 2):
    print(value)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))

# 列表推导式
squares = [value ** 2 for value in range(1, 11)]
print(squares)