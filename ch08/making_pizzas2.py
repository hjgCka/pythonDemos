#使用模块别名
#import pizza as p
#p.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

#导入模块中所有函数，但是最好不要这样。因为有可能命名会冲突。
#正确做法应该是，用到什么就导入什么；或者导入整个模块。
from pizza import *
make_pizza(16, 'mushrooms', 'green peppers')