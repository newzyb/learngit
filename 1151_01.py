# is a; has a 的用法

import random


class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


# 声明（定义）Car
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):  # road = r  road 与r 指向同一个地址空间
        ran_time = random.randint(1, 10)
        msg = '{}品牌的车，在{}上，以{}速度，行驶了{}小时。'.format(self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的车，速度为：{}'.format(self.brand, self.speed)


# 创建实例化对象
r = Road('京藏高速', 12000)
print(f'{r.name}--------> 初始(class Road)的名字。')

r.name = '京哈高速'
audi = Car('奥迪', 120)
print(f'修改后，Road的名字：------> {r.name}')
print(audi)

audi.get_time(r)    #对象
