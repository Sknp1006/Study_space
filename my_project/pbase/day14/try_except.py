#try_except.py

def div_apple(n):
    print("%d个苹果你想分给几个人?" % n)
    s = input('请输入人数:')
    count = int(s) #<---可能触发ValueError错误
    result = n / count  #<---可能触发ZeroDivisionError错误
    print("每人分了", result, '个苹果')


try:
    div_apple(10)
    print("分苹果成功")
# except ValueError as VE:
#     print("分苹果失败,苹果被收回", VE)
# except ZeroDivisionError:
#     print("没人分苹果,苹果被收回!")
except (ValueError, ZeroDivisionError):
    print("错啦")
else:
    print("此try语句内未发生任何异常")  #div_apple无任何异常时执行
    
print("程序正常结束")


# except ValueError:
#     print()
# except:
#     print()