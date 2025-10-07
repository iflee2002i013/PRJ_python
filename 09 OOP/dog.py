# 规定类名首字母大写，多个单词用驼峰法
class Dog:
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性 name 和 age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Chill', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()