#二分查找

#原始数据 value - [1,2,3,4,5,6,7,8,9,10,11,12,13]
#待查找数据 key - 9

def binary(value, key):
    #获取左侧和右侧对应下标值
    left = 0
    right = len(value) - 1
    while left <= right:
        #获取中间值对应的下标
        middle = (left + right) // 2
        #比较中间值与要查找的数据
        #若相等
        if value[middle] == key:
            #若相等,查找成功返回对应下标值
            return middle
        elif value[middle] < key:
            #则在右侧继续查找
            left = middle + 1
        else:
            #则在左侧继续查找
            right = middle - 1
    #如果遍历完仍未找到
    #查找失败,返回-1
    return -1

if __name__ == '__main__':
    value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    key = 9
    res = binary(value, key)
    if res == -1:
        #查找失败
        print('查找失败')
    else:
        #查找成功
        print("下标为", res)