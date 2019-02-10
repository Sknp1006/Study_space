# import time
# while True:
#     t = time.localtime()
#     print("  %02d:%02d:%02d" %(t[3], t[4], t[5]), end='\r')
#     #print("  %02d:%02d:%02d" %(t[3:6]), end='\r')
#     time.sleep(1)

# #闹钟1
# import time
# def clock(hour, min):
#     time = hour + ':' + min + ':' + '00'
#     return time
# hour = input("请输入小时:")
# min = input("请输入时间:")
# while True:
#     now_time = time.asctime()[11:19]
#     print(now_time)
#     time.sleep(1)
#     if clock(hour, min) == now_time:
#         print("时间到!!!")
#         break

#闹钟2
def run_alarm(hour, minute):
    '''此函数用来等待时间,当时间到设定时间时,打印时间到!!!'''
    import time
    while True:
        t = time.localtime()
        print("  %02d:%02d:%02d" %(t[3:6]), end='\r')
        #print("  %02d:%02d:%02d" %(t[3:6]), end='\r')
        time.sleep(1)
        if t[3:5] == (hour, minute):
            return
        
h = int(input("请输入小时:"))
m = int(input("请输入时间:"))
run_alarm(h, m)