# s = 'abdcdkleivnefdsfxx'
# d = {}
# for ch in s:
#     if ch in d:
#         d[ch] += 1
#     else:
#         d[ch] = 1
# d = sorted(d.items())
# for t in d:
#     print("%s:%d" %t[0:2])
# print(d)

# vocabulary = {}
# while True:
#     word = input("请输入一个单词:")
#     if not word:
#         print("输入结束")
#         break
#     else:
#         jieshi = input("请输入单词的解释:")
#         vocabulary[word] = jieshi

# while True:
#     word = input("请输入要查询的单词:")
#     if word == 'quit()':
#         break
#     try:
#         print(word, ':', vocabulary[word])
#     except KeyError as KE:
#         print("暂无该单词:", KE)

# L = ['tarena', 'xiaozhang', 'hello']
# d = [6,9,5]
# Z = zip(L, d)
# iter(Z)
# print(next(Z))
# print(next(Z))
# print(next(Z))

def glob():
    g = 1
    g = g + 1
    # global g
    print(g)
    print(locals())
glob()
print(globals())
