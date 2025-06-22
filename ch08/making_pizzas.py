#导入整个模块
#import pizza
#pizza.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

#导入特定函数，并给函数设置别名
from pizza import make_pizza as mp
mp(16, 'mushrooms', 'green peppers')