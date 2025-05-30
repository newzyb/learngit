class Cat:
    type = '猫'

    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

    def catch(self, color, weight):
        self.color = color
        self.weight = weight
        print('{}的颜色是：{}，体重是：{}斤'.format(self.name,self.color,self.weight))

    def eat(self,food):
        self.food = food
        print('{}正在吃{}。'.format(self.name,self.food))

    def sleep(self,hour):
        if hour<5:
            print('睡眠不足，赶快去睡觉吧！')
        else:
            print('睡好了，赶快去抓{}吧！'.format(self.food))

    def show(self):
        print('猫的详细信息：')
        print(self.name,self.age, self.color)

c1 = Cat('huahua', 8,'yellow')
c1.catch('黑色', 2)
c1.eat('老鼠')
c1.sleep(6)
c1.show()
