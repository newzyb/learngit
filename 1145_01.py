# 静态方法

class Person:
    __age = 20

    def __init__(self, name):
        self.name = name

    @classmethod
    def show(cls):
        print('初始属性默认年龄：', cls.__age)

    @staticmethod
    def test():
        Person.__age = 22
        print('修改后的年龄是：', Person.__age)


s = Person.show()

Person.test()
