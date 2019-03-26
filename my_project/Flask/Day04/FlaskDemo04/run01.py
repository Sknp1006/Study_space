from flask import Flask
# 导入SQLAlchemy用于创建数据库的实例
from flask_sqlalchemy import SQLAlchemy

# 导入pymysql 并将其视为 mysqldb
# import pymysql
# pymysql.install_as_MySQLdb()

app = Flask(__name__)
# 通过app指定连接数据库的信息
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/flask"
# 取消SQLAlchemy的信号追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 创建数据库应用实例 - db
db = SQLAlchemy(app)


# 创建实体类-Users,映射到数据库中表名叫users表
# 创建字段-id,主键,自增
# 创建字段-username,长度为80的字符串,不允许为空,值唯一,增加索引
# 创建字段-age,整数,允许为空
# 创建字段-email,长度为120的字符串,值唯一,不允许为空
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(80),
        nullable=False, unique=True, index=True
    )
    age = db.Column(
        db.Integer, nullable=True
    )
    email = db.Column(
        db.String(120),
        unique=True, nullable=False
    )

# 将创建好的实体类映射回数据库,生成表
# (前提:数据表不存在)
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
