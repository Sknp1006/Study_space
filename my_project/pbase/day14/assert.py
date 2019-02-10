def get_score():
    s = int(input("请输入学生成绩:"))
    assert 0 <= s <= 100, '成绩超出范围'
    return s

try:
    score = get_score()
except ValueError as err:
    print("请输入数字!!!!")
except AssertionError as AE:
    print("成绩超出范围!!!")