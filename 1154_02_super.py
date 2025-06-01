# super 父类（基类）

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭...')

    def run(self):
        print(self.name + '正在跑步...')


class Student(Person):
    def __init__(self, name, age, clazz):
        super().__init__(name, age)     # 调用父类的__init__
        self.clazz = clazz


class Employee(Person):
    def __init__(self, name, age, salary, manager):
        super().__init__(name, age)
        self.salary = salary
        self.manager = manager


class Doctor(Person):
    def __init__(self, name, age, patients):
        super(Doctor, self).__init__(name, age)
        self.patients = patients


s = Student('jcak', 18, 'python1905')
s.run()

e = Employee('Tom', 23, 10000, 'king')
e.run()

lists = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
d = Doctor('lucy', 30, lists)
d.run()

