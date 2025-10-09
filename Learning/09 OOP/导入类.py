# 每个类可以单独成立一个文件，作为类导入
# 以本文件夹内的car.py为例
from car import Car 

my_new_car = Car('audi','a4',2025)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

# 可以从一个文件（模块）中导入多个类
from _类_的组合使用 import Car,ElectricCar,Battery

my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery() # 在这里就要调用子类的子类的属性
my_leaf.battery.get_range() 


