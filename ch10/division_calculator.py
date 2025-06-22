print("Give me tow numbers, and I'll divide them")
print("Enter 'q' to quit")

answer = None
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        #这里报错的话，给answer赋值就不会执行
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero")
    #只要try代码块成功执行才需要继续执行的代码，应放入else块
    else:
        print(answer)
