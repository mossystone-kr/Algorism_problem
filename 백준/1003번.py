import sys

a = int(sys.stdin.readline())
data = []

for i in range(a):
    data.append(int(sys.stdin.readline()))

di = [0] * 40
di[0] = 1

def fun(k):
    if di[k-1]:
        return di[k-1]
    else:
        return fun(k-1) + fun(k-2)