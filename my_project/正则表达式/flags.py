import re

#re.I 忽略大小写
# s = "Hello world"
# pattern = r'hello'
# regex = re.compile(pattern, flags=re.I)  #忽略大小写

#re.A 使用ASCII字符
# s = "Hello world, 你好"
# pattern = r'\w+'
# regex = re.compile(pattern, flags=re.A)  #用ASCII匹配

#re.S 使 . 匹配\n
# s = '''Hello world
# nihao China
# '''
# pattern = r'.+'
# regex = re.compile(pattern, flags=re.S)  #匹配到换行符\n

#M 匹配每行开头结尾
# s = '''Hello world
# nihao China'''
# pattern = r'world$'
# regex = re.compile(pattern, flags=re.M)  #能匹配每一行的开头和结尾

#X 给正则加注释
# s = "abcdefgh"
# pattern = r'''(ab)  #第一行分组
# \w+   #任意字符串
# (?P<dog>ef)  #dog组
# '''
# regex = re.compile(pattern, flags=re.X)  #[('ab', 'ef')]





l = regex.findall(s)
print(l)

