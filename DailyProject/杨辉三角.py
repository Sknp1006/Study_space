def get_next_line(L):
    RL = [1]
    for i in range(len(L)-1):
        x = L[i] + L[i + 1]
        RL.append(x)
    RL.append(1)
    return RL

def get_yanghui_list(n):
    L = []
    line = [1]
    while len(L) < n:
        L.append(line)
        line = get_next_line(line)
    return L

def get_yanghui_string(L):
    RL = []
    for line in L:
        temp = [str(x) for x in line]
        s = ' '.join(temp)
        RL.append(s)
    return RL

def print_yanghui(L):
    w = len(L[-1])
    for s in L:
        print(s.center(w))

L = get_yanghui_list(6)
L2 = get_yanghui_string(L)
print_yanghui(L2)