#冒泡排序

#原始数据 - value
#[100, 190, 165, 170, 155, 108, 139, 175, 160, 180]


def bubble(value):
    #外部循环: 对应走访数据的次数
    for i in range(len(value)-1):
    #内部循环: 对应每次走访数据时,相邻数据对比的次数
        for j in range(len(value)-i-1):
            #取从小到大排序
            #如果前者大于后者,则两者交换
            if value[j] > value[j+1]:
                value[j],value[j+1] = value[j+1], value[j]
    print("遍历次数:", i+1)

if __name__ == '__main__':
    #原始数据
    value = [100, 190, 165, 170, 155, 108, 139, 175, 160, 180]
    #冒泡排序
    bubble(value)
    print("排序后:", value)