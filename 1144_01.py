
'''
类方法
1:它们可以直接访问或修改类属性（定义在类级别，所有实例共享的属性）
2:工厂模式（Factory Pattern）：当你需要提供多种方式来创建类的实例时，类方法是理想的选择。
它们可以使代码更具可读性，因为方法名可以清楚地描述对象的创建方式（例如 from_string, from_json, from_birth_year）。
3:操作类级别的数据：当方法需要访问或修改类属性（所有实例共享的数据），而不是实例属性时。
4:与类本身相关的工具方法：有时你可能有一些工具函数，它们逻辑上属于某个类，但不需要特定实例的数据。
虽然静态方法（@staticmethod）也可以用于此目的，但如果该工具方法可能需要访问类本身（例如，为了创建该类的实例或访问其他类属性/方法），
那么类方法更合适。
'''

class Dog:
    __age = 18

    def __init__(self,nickname):
        self.nickname = nickname

    def run(self):
        print('{}在院子里跑来跑去。'.format(self.nickname))

    def eat(self):
        print('吃饭。。。')
        self.run()  # 类中的方法调用，需要通过self.方法名()

    @classmethod
    def update_age(cls):
        cls.__age = 20
        print(cls.__age)

    @classmethod
    def show_age(cls):
        print('修改后的年龄：', cls.__age)

Dog.update_age()

Dog.show_age()


