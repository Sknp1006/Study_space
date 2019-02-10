def get_age(n):
    if n == 1:
        return  10
    return get_age(n-1)+2
    
print(get_age(3))
print(get_age(5))
