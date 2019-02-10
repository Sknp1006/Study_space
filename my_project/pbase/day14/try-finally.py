#此示例以煎鸡蛋的控制程序来示意try-finally语句应用场景

# def fry_egg():
#     try:
#         print("打开天然气点燃...")
#         try:
#             count = int(input("请输入鸡蛋个数:"))
#             print("完成煎鸡蛋,共煎了%d个鸡蛋" % count)
#         finally:
#             print("关闭天然气")    #<---此事必须要做
#     except ValueError:
#         print("煎鸡蛋失败")
        
# fry_egg()



def fry_egg():
    print("打开天然气点燃...")
    try:
        count = int(input("请输入鸡蛋个数:"))
        print("完成煎鸡蛋,共煎了%d个鸡蛋" % count)
    finally:
        print("关闭天然气")    #<---此事必须要做

try:
    fry_egg()
except ValueError:
    print("煎鸡蛋失败")
        