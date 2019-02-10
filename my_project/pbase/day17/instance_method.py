class Dog:
    '''此类用于描述一种小动物的行为和属性'''
    def eat(self, food):
        print("ID为:", id(self), "小狗正在吃:", food)
    
    def sleep(self, hour):
        print("小狗睡了", hour, "小时")
    
    def play(self, obj):
        print("小狗正在玩", obj)


dog1 = Dog()
dog1.eat('骨头')
dog1.sleep(1)
dog1.play('蛇')

dog2 = Dog()
dog2.eat('粥')
dog2.play('飞机')
dog2.sleep(3)
