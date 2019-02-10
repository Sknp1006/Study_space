#冒泡排序 - 优化

#原始数据 - value
#[100, 190, 165, 170, 155, 108, 139, 175, 160, 180]


def bubble(value):
    #外部循环: 对应走访数据的次数
    for i in range(len(value)-1):
        #设置标志位
        flag = False
        
        #内部循环: 对应每次走访数据时,相邻数据对比的次数
        for j in range(len(value)-i-1):
            #取从小到大排序
            #如果前者大于后者,则两者交换
            if value[j] > value[j+1]:
                value[j],value[j+1] = value[j+1], value[j]
                #数据交换标志为True
                flag = True

        #检查是否进行数据交换
        #若未发生数据交换,则证明剩余数据有序
        #无需进行下一次数据的走访
        if flag == False:
            #跳出外部循环
            break
    print("遍历次数:", i+1)


if __name__ == '__main__':
    #原始数据
    value = [200, 100, 108, 139, 155, 160, 165, 170, 175, 180, 190]
    #冒泡排序
    bubble(value)
    print("排序后:", value)