import pymysql

host = 'localhost'     #服务器地址
user = 'root'          #用户名
password = '123456'    #密码
dbname = 'dict'        #指定数据库

f = open('./dict.txt')
#连接数据库
db = pymysql.connect(host, user, password, dbname)
#获取游标
cursor = db.cursor()

for line in f:
    tmp = line.split(' ')
    word = tmp[0]
    interpret = ' '.join(tmp[1:]).strip()
#    print(word, interpret) 

    #执行SQL语句
    sql = '''insert into words (word, interpret)
            values("%s", "%s")'''%(word, interpret)
    try:
        cursor.execute(sql)   #执行SQL语句
        db.commit()
    except Exception:
        db.rollback()
f.close()

cursor.close()
db.close()