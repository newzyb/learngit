# 静态方法练习

class Person:
    __age = 18

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def action(self):
        print(f'{self.name}正在打篮球.')

    @classmethod
    def test(cls, name, age):
        cls.name = name
        cls.age = age
        print(f'{cls.name}前年的年龄是：{cls.__age}。')

    @staticmethod
    def show():
        Person.__age = 20
        print(f'今年的年龄是：{Person.__age}。' )


p = ('李明', 17)

p1 = Person.test('张三', 22)


p2 = Person.show()
