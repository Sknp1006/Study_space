#pymysql插入示例

import pymysql
from db_conf import * #导入配置

try:
    #连接数据库
    conn = pymysql.connect(host, user, password, dbname)
    #获取游标
    cursor = conn.cursor()
    #执行SQL语句
    sql = '''insert into acct 
      values('622345000010', 'Robert', 'C0010', 1, date(now()), 1, 33.00)
    '''
    cursor.execute(sql)   #执行SQL语句
    conn.commit()         #提交事务
    print("Insert OK")    #
except Exception as e:
    print("数据库插入异常")
    print(e)
finally:
    cursor.close()
    conn.close()

