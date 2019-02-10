#acct_manage.py
#账户管理系统,实现帐户增删改查
import pymysql
from db_conf import * 

db_conn = None   #连接对象

#连接数据库函数
def conn_database():
    global db_conn
    db_conn = pymysql.connect(host, user, password, dbname)
    if not db_conn: # 连接失败
        print('连接数据库失败')
        return -1
    else:           #连接成功
        return 0


#关闭数据库
def close_database():
    global db_conn
    if db_conn:     #判断对象不为空
        db_conn.close()


#打印菜单
def print_menu():
    menu = '''
    ------------------账户管理系统------------------
            1 - 查询账户信息
            2 - 新建账户
            3 - 修改账户
            4 - 删除账户
            5 - 退出
    '''
    print(menu, end='\r')
    return 


#查询账户,如果用户输入帐号,则以帐号为输入条件进行查询
#如果用户不输入,则查询所有账户
def query_acct():
    acct_no = input('请输入查询的帐号:')
    if acct_no and acct_no != "":   #用户输入了账户
        sql = '''
        select * from acct
        where acct_no = '%s'
        '''%acct_no
    else:    #用户不输入账户,查询所有
        sql = 'select * from acct'
    
    global db_conn
    cursor = db_conn.cursor()  #获取游标
    try:
        cursor.execute(sql)         #执行SQL
        result = cursor.fetchall()  #获取所有数据
        for r in result:            #遍历,打印
            acct_no = r[0]          #帐号
            acct_name = r[1]        #户名
               #余额
            if r[6]:
                balance = float(r[6])
            else:
                balance = 0.00
            print("帐号:%s, 户名:%s, 余额:%.2f" %(acct_no, acct_name, balance))
    except Exception as e:
        print("查询异常")
        print(e)
    return


#新增用户
def new_acct():   
    try:
        acct_no = input("请输入帐号:")
        acct_name = input("请输入户名:")
        acct_type = input("请选择账户类型 1-借记卡 2-理财卡:")
        balance = float(input("请输入开户金额:"))
        assert acct_type in ['1', '2']    #判断acct_type是否合法
        assert balance >= 10.00
        type = int(acct_type)    #账户类型转换为整数型

        #拼装SQL语句,执行插入
        sql = '''
               insert into acct(acct_no, acct_name, acct_type, balance)
               values('%s', '%s', %d, %.2f)
        '''%(acct_no, acct_name, type, balance)

        #获取游标,执行
        global db_conn
        cursor = db_conn.cursor()
        cursor.execute(sql)    #执行
        db_conn.commit()       #提交
        print("Insert OK")
    except Exception as e:
        db_conn.rollback()     #回滚事务
        print("数据插入失败")    
        print(e)
    return


def update_acct():
    try:
        acct_no = input("请输入要修改的帐号:")
        if acct_no and acct_no != '':
            balance_mod = int(input("输入修改金额:"))
            sql = '''update acct set balance = balance + %d where acct_no = '%s' '''%(balance_mod, acct_no)
        else:
            raise ValueError
        global db_conn
        cursor = db_conn.cursor()
        cursor.execute(sql)
        db_conn.commit()
        print("修改成功")
    except Exception as e:
        db_conn.rollback()
        print("修改失败")
        print(e)
    except ValueError as v:
        db_conn.rollback()
        print("输入的帐号不合法")
        print(v)
    return


def delete_acct():
    try:
        acct_no = input("请输入要删除的帐号:")
        if acct_no and acct_no != '':
            sql = '''
                    delete from acct where acct_no = '%s'
            '''%acct_no
        else:
            raise ValueError
        global db_conn
        cursor = db_conn.cursor()
        cursor.execute(sql)
        db_conn.commit()
        print("删除成功")
    except Exception as e:
        db_conn.rollback()
        print("删除失败")
        print(e)
    except ValueError as v:
        db_conn.rollback()
        print("输入的帐号不合法")
        print(v)
    return
    

#main()
def main():
    # 连接数据库
    if conn_database() < 0:
        return
    #循环打印菜单,根据选择的菜单
    #调用不同函数进行处理
    while True:
        print_menu()  #打印菜单
        oper = input("请选择操作:")
        if not oper:  #未输入值
            continue
        if oper == '1':  #查询
            query_acct()
        elif oper == '2': #新建
            new_acct()
        elif oper == '3': #修改
            update_acct()
        elif oper == '4': #删除
            delete_acct()
        elif oper == '5': #退出
            break
        else:
            print("请输入正确的值")
            continue
    
    #关闭数据库
    close_database()


#主函数
if __name__ == '__main__':
    main()

