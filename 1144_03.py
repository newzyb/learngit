'''
例子2：访问和修改类属性
类方法可以用来管理属于类本身的属性，而不是属于某个特定实例的属性。
'''


class Car:
    total_cars_produced = 0  # 这是一个类属性

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars_produced += 1  # 每创建一个实例，类属性就增加

    @classmethod
    def get_total_cars_produced(cls):
        # cls 指的是 Car 类本身
        # 通过 cls 可以访问类属性
        return cls.total_cars_produced

    @classmethod
    def set_production_goal(cls, goal):
        cls.production_goal = goal  # 设置一个新的类属性
        print(f"汽车生产目标设置为: {cls.production_goal} 辆")

    def display_info(self):
        print(f"品牌: {self.brand}, 型号: {self.model}")


# 创建一些 Car 实例
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("Tesla", "Model S")

# 使用类方法获取类属性的值
total_produced = Car.get_total_cars_produced()
print(f"总共生产的汽车数量: {total_produced}")

# 使用类方法设置一个新的类属性
Car.set_production_goal(10000)
print(f"当前生产目标: {Car.production_goal}")

# 也可以通过实例调用类方法，cls 仍然是 Car 类
# print(f"通过实例调用获取总数: {car1.get_total_cars_produced()}")
