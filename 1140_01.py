'''
self根据每个方法的不同，动态的创建。
'''

class Phone:
    def __init__(self):
        self.price= 4999
        self.brand = "huawei"

    def call(self):
        print('我的手机品牌是：{}，价格为：{}'.format(self.brand, self.price))


p1 = Phone()
p1.call()

p2 = Phone()
p2.brand = "xiaomi"
p2.price = 5999
p2.call()

