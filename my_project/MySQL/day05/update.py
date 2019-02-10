#pymysql插入示例

import pymysql
from db_conf import * #导入配置

try:
    #连接数据库
    conn = pymysql.connect(host, user, password, dbname)
    #获取游标
    cursor = conn.cursor()
    #执行SQL语句
    sql = '''Update acct set balance = balance + 1000 where acct_no = '622345000010'
    '''
    cursor.execute(sql)   #执行SQL语句
    conn.commit()         #提交事务
    print("修改笔数:%d" %cursor.rowcount)    #
except Exception as e:
    print("数据库修改异常")
    print(e)
finally:
    cursor.close()
    conn.close()

