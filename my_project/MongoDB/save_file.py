from pymongo import MongoClient
import bson.binary

conn = MongoClient('localhost', 27017)
db = conn.image
myset = db.boy

#读取图片
with open('image.jpg', 'rb') as f:
    data = f.read()

#转换mongo格式
content = bson.binary.Binary(data)

#将内容插入集合
doc = {'filename': 'image', 'data': content}
myset.insert(doc)

###########################################################
img = myset.find_one({'filename':'image.jpg'})

#写入本地
with open('image.jpg', 'wb') as f:
    f.write(img['data'])
    
conn.close()
