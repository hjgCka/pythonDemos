def greet_users(names):
    """向列表中的每个用户发出简单的问候"""
    for name in names:
        msg = f"hello {name.title()}"
        print(msg)

usernames = ['jack', 'john', 'paul']
greet_users(usernames)

#创建了名为toppings的元组
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('mushrooms', 'green peppers', 'extra cheese')

# **创建了名为user_info的字典，该字典包含函数收到的其它所有键值对
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('jimi', 'hendrix',
                             location='princeton',
                             field='physics')
print(user_profile)