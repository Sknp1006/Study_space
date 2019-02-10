import re

pattern = r'\d+'

s = "2018年中国经济增长6.6%,与2017年基本持平,2019面临很多困难"

#match对象属性
it = re.finditer(pattern, s)

# print(dir(next(it)))
# for i in it:
#     print(i.group())

# try:
#     obj = re.fullmatch(r'\w+', 'hello1973')
#     print(obj.group())
# except AttributeError as e:
#     print(e)

# obj = re.match(r'[A-Z]\w+', 'Hello 1973')
# print(obj.group())

obj = re.search(r'\d+', s)
print(obj.group())