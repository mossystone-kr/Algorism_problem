import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = str(a*b*c)
e = [0,0,0,0,0,0,0,0,0,0]
for j in range(10):
    f = 0
    for i in range(len(d)):
        if int(d[i]) == j:
            f += 1
    print(f)