def func(**kwargs):
    print("关键字参数的个数是:",len(kwargs))
    print("kwargs=", kwargs)
    return kwargs

func(name='魏明泽', age=35, address= '朝阳区')
func(a=1, b=2, c=3, d="ABC", e=[1,2,3])
