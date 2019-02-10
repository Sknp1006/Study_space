#快速排序

#原始数据 - value
#[80,70,30,50,69,78,90,100,65,88]

def quick(value):
    #递归退出条件
    if len(value) < 2:
        return value
    
    #设置关键数据
    mark = value[0]
    #找出所有小于关键数据的
    small = [x for x in value if x < mark]
    #找出所有等于关键数据的
    equal = [x for x in value if x == mark]
    #找出所有大于关键数据的
    big = [x for x in value if x > mark]

    #从小到大顺序排列
    return quick(small) + equal + quick(big)

if __name__ == '__main__':
    value = [80,70,30,50,69,78,90,100,65,88]
    print(quick(value))
