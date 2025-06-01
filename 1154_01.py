# is a 的用法

class Person:
    def __init__(self, name):
        self.name = name
        self.age = 18

    def eat(self):
        print(self.name + '正在吃饭...')

    def run(self):
        print(self.name + '正在跑步...')


class Student(Person):
    def __init__(self,name):
        print('--------------student的int')
        # 如何调用父类__init__
        super().__init__(name)  # super() 父类对象


class Employee(Person):
    pass

class Doctor(Person):
    pass


s = Student('jcak')
s.run()
e = Employee('lily')
e.run()
d = Doctor('tom')
d.run()