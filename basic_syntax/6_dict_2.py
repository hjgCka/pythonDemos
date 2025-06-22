user_0 = {
    'name': 'Jack',
    'first': 'Jack',
    'last': 'Paul'
}

for key, value in user_0.items():
    print(f"{key}: {value}")

# 相当于 for key in user0
for key in user_0.keys():
    print(f"{key}: {user_0[key]}")

# 遍历时，按照插入dict的顺序
# user_0.values()

# set
languages = {'python', 'rust', 'c', 'java', 'kotlin'}
print(languages)

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(f"you ordered a {pizza['crust']}-crust pizza"
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
