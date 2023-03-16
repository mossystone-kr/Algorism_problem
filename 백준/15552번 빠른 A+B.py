import sys

a = int(sys.stdin.readline())
r = []
for i in range(a):
    b, c = map(int, sys.stdin.readline().split())
    r.append(b+c)

for k in r:
    print(k)