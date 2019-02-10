v = 100
def fn(v):
    global v
    v = 200
    print(v)
fn(300)
print("全局的v=", v)

