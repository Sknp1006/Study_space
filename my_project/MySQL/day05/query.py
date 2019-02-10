#pymysql查询示例
# 第一步:导入pymysql模块
import pymysql

# 第二步:连接数据库
host = 'localhost'     #服务器地址
user = 'root'          #用户名
password = '123456'    #密码
dbname = 'bank'        #指定数据库
conn = pymysql.connect(host, user, password, dbname)

# 第三步:创建游标对象(cursor),通过调用数据库连接对象获得游标
cursor = conn.cursor()

# 第四步:利用cursor对象执行SQL语句
sql = 'select * from acct;'
cursor.execute(sql)    #执行SQL语句

#取出查询结果,并打印
# result = cursor.fetchone()
# print(result)
# result = cursor.fetchmany(2)       #游标会记住取到的位置
# print(result)

result = cursor.fetchall()
for r in result:
    acct_no = r[0]     #帐号
    acct_name = r[1]   #户名
    if r[6]:           #判断是否为空值
        balance = float(r[6])    #余额
    else:
        balance = 0.00 #余额为空,默认为0
    print("帐号:%s, 户名:%s, 余额:%.2f" %(acct_no, acct_name, balance))

# 第五步:如果执行了增删改,提交事务,出错则回滚
#未修改不用提交

# 第六步:关闭游标对象
cursor.close()

# 第七步:关闭数据库连接对象
conn.close()



