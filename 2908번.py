import sys

a,b = map(str,sys.stdin.readline().split())
a = int(a[2])*100 + int(a[1])*10 + int(a[0])
b = int(b[2])*100 + int(b[1])*10 + int(b[0])
if a>b:
    print(a)
else:
    print(b)