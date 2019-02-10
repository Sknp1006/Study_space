import re

pattern = r"\d+"
pattern = r"(\w+):(\d+)"
s = "告别2018,展望2019"
s = "张:1994,李:1955"

#直接用re调用
# l = re.findall(pattern, s)
# print(l)

#compile调用
# regex = re.compile(pattern)
# l = regex.findall(s, pos=0, endpos=10)
# print(l)

# l = re.split(r'\s+', 'Hello   world    fdfasd')
# print(l)

s = re.subn(r'\s+', '##', "hello world  n ihao kitty")
print(s)
# ('hello##world##n##ihao##kitty', 4)



# [('张', '1994'), ('李', '1955')]

