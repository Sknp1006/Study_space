from pymongo import MongoClient

#创建数据库连接
conn = MongoClient('localhost',27017)

#创建数据库对象
db = conn.stu 

#创建集合对象
myset = db['class4']

#操作数据
# print(dir(myset))


#插入文档
# myset.insert_one({'name':'张铁林', 'King':'乾隆'})
# myset.insert_many([{'name':'张国立', 'King':'康熙'}, \
#                 {'name':'陈道明', 'King':'康熙'}])
# myset.insert({'name': '唐国强', 'King': '雍正'})
# myset.insert([{'name': '陈建斌', 'King': '雍正'}, \
#             {'name': '聂远', 'King': '乾隆'}])

# myset.save({'_id': 1, 'name': '吴奇隆', 'King': '四爷'})
# myset.save({'_id': 1, 'name': '郑少秋', 'King': '乾隆'})


#查找文档
# cursor = myset.find({'King': '乾隆'}, {'_id':0})
# cursor = myset.find({'name': {'$exists':True}}, {'_id':0})
# print(cursor)

#循环获取每一条文档
# for i in cursor:
#     print(i['name'])

# print(cursor.next())  #获取下一条文档
# print(cursor.next())  #获取下一条文档


# for i in cursor.skip(1).limit(3):
#     print(i)

#注意排序写法同mongo shell 不同,用元组表达
# for i in cursor.sort([('name', 1)]):
#     print(i)

#find_one直接返回字典
# dic = {'$or': [{'King': '乾隆'}, {'name': '陈道明'}]}
# d = myset.find_one(dic)
# print(d)


#修改操作
# myset.update_one({'King':'康熙'}, {'$set':{'King_name': '玄烨'}}, upsert=True)

# myset.update_many({'King': '乾隆'}, {'$set':{'King_name': '弘历'}})


# #删除操作
# myset.delete_one({'King': '乾隆'})
# myset.delete_many({'King_name':{'$exists': False}})
# myset.delete_one({'name':"张国立", 'King_name':{'$exists':False}})

#符合操作
# print(myset.find_one_and_delete({'name':'郑少秋'}))



#关闭连接
conn.close()