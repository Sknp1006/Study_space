def func(*args):
    print("实参的个数是:", len(args))
    print("args=", args)
    #print(sum(args))

func()
func(1,2,3,4)
#func(1,2,3,4,'AAA','BBB')
func(*'ABCDEFG')

