import sys

dot, line, start =  map(int,sys.stdin.readline().split())
v1,v2 = [],[]

for _ in range(line):
    a, b = map(int,sys.stdin.readline().split())
    v1.append(b)
    v2.append(a)
