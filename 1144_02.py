'''
例子1：使用类方法作为工厂方法
假设我们有一个 Person 类，通常我们通过姓名和年龄来创建 Person 对象。
但有时我们可能想通过姓名和出生年份来创建对象。这时，类方法就非常有用。
'''

import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = datetime.date.today().year
        age = current_year - birth_year
        # cls 指的是 Person 类本身
        # cls(name, age) 等同于 Person(name, age)
        return cls(name, age)

    def display_info(self):
        print(f"姓名: {self.name}, 年龄: {self.age}")

# 使用常规构造函数创建对象
person1 = Person("张三", 30)
person1.display_info()

# 使用类方法 from_birth_year 作为工厂方法创建对象
person2 = Person.from_birth_year("李四", 1995)
person2.display_info()

# 也可以通过实例调用类方法，但不常见，因为 cls 仍然是 Person 类
# person_instance = Person("王五", 25)
# person3 = person_instance.from_birth_year("赵六", 2000)
# person3.display_info()