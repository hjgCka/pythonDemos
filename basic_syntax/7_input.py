# 向用户显式的提示
message = input("tell me something, and I will repeat it back to you: ")
print(message)

number = input("enter a number: ")
number = int(number)
if number % 2 == 0:
    print(f"the number {number} is even")
else:
    print(f"the number {number} is odd")