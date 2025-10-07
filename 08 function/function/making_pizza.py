import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

# 从特定的模块中导入函数 然后别名化
from pizza import make_pizza as mp

# 使用*号导入模块中的所有函数
from pizza import *
# 注意，这样做会导入模块中的所有函数。
# 当模块中的函数和当前文件中的函数同名时，可能会引发问题。
# 并且，很有可能导致阅读代码的人无法确定某个函数是从哪里导入的。


