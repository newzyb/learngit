'''
__init__:魔术方法
'''


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        self.food = food
        print('{}正在吃{}。'.format(self.name, self.food))

    def run(self, km):
        self.km = km
        print('{}今年{}岁了，正在跑{}km。'.format(self.name, self.age, self.km))


p1 = Person('lisi', 18)
p1.eat('zhaji')
p1.run(5)

p2 = Person('zhangsan', 20)
p2.name = '张三'
p2.eat('hongshaorou')
p2.run(10)

p3 = Person('liliu', 22)
p3.eat('shizitou')
p3.run(15)
