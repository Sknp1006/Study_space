class Dog:
    def eat(self, food):
        print(self.color, '的', self.kinds, "正在吃:", food)
        self.last_food = food #让每次吃事物的狗记住吃的是什么
    
    def food_info(self):
        print(self.color, '的', self.kinds, '上次吃的是', self.last_food)

dog1 = Dog()  #创建一个实例
dog1.color = "白色"  #为dog1对象添加color属性,绑定为'白色'
dog1.kinds = '京巴'  #添加kinds属性
dog1.eat('骨头')
# print(dog1.color, '的', dog1.kinds)

dog2 = Dog()
dog2.color = '灰色'
dog2.kinds = '二哈'
dog2.eat('胖次')

dog1.food_info()
dog2.food_info()