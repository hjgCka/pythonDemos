cars = ['audi', 'bmw', 'benz', 'honda']

for car in cars:
    # if car != 'bwm':
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 使用 and or，组合多个条件
# in not in，检查是否再列表
car = 'audi'
if car in cars:
    print(f"{car.title()} is in cars")

age = 20
if age < 14:
    print("your admission cost is $0")
elif age < 18:
    print("your admission cost is $5")
else:
    print("your admission cost is $10")

# 确定列表非空
toppings = []
if toppings:
    for topping in toppings:
        print(topping)
else:
    print("no toppings")
