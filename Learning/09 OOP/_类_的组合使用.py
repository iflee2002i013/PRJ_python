class Car:
    '''一次模拟汽车的简单尝试'''
    def __init__(self,make,model,year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """将里程表读书设置为指定的值"""
        self.odometer_reading = mileage

my_new_car = Car('audi','a4',2025)
my_new_car.odometer_reading = 25

print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()  

my_new_car.update_odometer(23)
my_new_car.read_odometer

# 创建独立的类并和其他类进行组合

class Battery:
    def __init__(self,battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电动汽车的行驶范围"""
        if self.battery_size == 40:
            range = 240
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        下面一行代码等于声明了以上内容
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    # 重写父类方法
    def update_odometer(self, mileage):
        """电动汽车里程表读书只能增加"""
        """实际意思是在子类中重新定义父类方法"""
""" 
my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery() # 在这里就要调用子类的子类的属性
my_leaf.battery.get_range() 
 """



