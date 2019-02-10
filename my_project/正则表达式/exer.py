import re

f = open('1.txt')
data = f.read()

# pattern = r"\b[A-Z]+\w*"  #单词
pattern = r'-?\d+\.?/?\d*%?'
l = re.findall(pattern, data)


print(l)
