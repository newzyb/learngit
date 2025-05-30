class Phone:
    brand = 'HuaWei'
    price = 29999
    type = 'mate 90'


    def call(self, *args, **kwargs):
        # note = '13837414928'
        print('{}正在打电话：{}'.format(self.name, self.note))

phoneA = Phone()
phoneA.name = 'xiaoyu'
phoneA.note = '13837414927'
phoneA.call()

phoneB = Phone()
phoneB.name = 'yuanyuan'
phoneB.note = '13837414928'
phoneB.call()

