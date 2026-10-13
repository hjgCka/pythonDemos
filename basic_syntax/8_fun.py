def greet_user(username):
    """显示简单的问候语
    这种是多行字符串，还是会占据内存，最好别这样用，当作注释不好"""
    print(f"hello {username.title()}")

greet_user('jack')

#位置实参
def describe_pet(animal_type, pet_name = 'tom'):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('cat', 'mimi')

#关键字实参
describe_pet(animal_type='dog', pet_name='tom')

#默认值，默认值从后往前排
describe_pet(animal_type='cat')
describe_pet('cat')