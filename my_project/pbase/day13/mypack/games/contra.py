#file : mypack/games/contra.py

def play():
    print("正在玩 魂斗罗 ...")

print("魂斗罗模块被加载")

def gameover():
    '''此函数示意包的相对导入,在当前contra.py模块中
    导入上一级(mypack)的menu.py里的show_menu,然后调用
    '''
    import time
    time.sleep(2)
    
    #绝对导入
    # from mypack.menu import show_menu
    
    #相对导入
    from ..menu import show_menu

    #错误导入
    # from ...mypack.menu import show_menu
    #ValueError: attempted relative import beyond top-level package

    show_menu()