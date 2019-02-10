from pymongo import MongoClient
import random as R

#创建数据库连接
conn = MongoClient('localhost',27017)

#创建数据库对象
db = conn.stu 

#创建集合对象
myset = db['class0']

#将没有性别域的文档删除
# myset.delete_many({'gender':{'$exists':False}})

#给所有文档增加一个域分数取值范围 60--100
lines = myset.find()
for line in lines:
    name = line['name']
    # print(type(name))
    Ch = R.randint(60, 100)
    Ma = R.randint(60, 100)
    En = R.randint(60, 100)

    myset.update_one({'name': name}, {'$set':{'score': {'Chinese': Ch, 'Math': Ma, 'English': En}}})

# res = myset.find({}, {'_id':0})
# for i in res:
#     print(i)

#聚合操作,查看所有女生的英语成绩排序,不显示_id项
l = [
    {'$sort':{'score.English':-1}}, \
    {'$match':{'gender': 'w'}},\
    {'$project':{'_id':0}}]
cursor = myset.aggregate(l)
for i in cursor:
    print(i)


conn.close()

