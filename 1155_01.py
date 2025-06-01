'''
特点：
    1、如果类中不定义__init__,调用父类 super class的__init__
    2、如果类继承父类也需要定义自己的__init__,就需要在当前类的__init__,调用一下父类的__init__.
    3、如何调用父类的__init__:
        super().__init__(参数)
        super(类名，对象).__init__(参数)
    4、如果父类有eat(),子类也定义一个eat方法，默认搜索的原则：先找当前类，再去找父类
        s.eat()
        override: 重写（覆盖）
        父类提供的方法不能满足子类的需求，就需要在子类中定义一个同名的方法，这种行为叫做：重写。
    5、子类的方法中也可以调用父类的方法：
        super().方法名（参数）
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "正在吃饭...")

    def run(self):
        print(self.name + '正在跑步...')


class Student(Person):
    def __init__(self, name, age, clazz):
        super().__init__(name, age)
        self.clazz = clazz

    def study(self, course):
        print('{}正在学习{}课程'.format(self.name, course))

    def eat(self, food):
        super().eat()
        print(self.name + "正在吃饭...,喜欢吃：" + food)


class Employee(Person):
    def __init__(self, name, age, salary, manager):
        super().__init__(name, age)
        self.salary = salary
        self.manager = manager


class Doctor(Person):
    def __init__(self, name, age, patients):
        super(Doctor, self).__init__(name, age)
        self.patients = patients


s = Student('阿文', 18, 'python1905')
s.run()
s.study('python基础')
s.eat('满汉全席')

e = Employee('tom', 23, 10000, 'king')
e.run()

lists = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
d = Doctor('lucy', 30, lists)
d.run()