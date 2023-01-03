import sys

a = int(sys.stdin.readline())

m,n = 0,0

for i in range(1,a+1):
    if i % 256 == 0:
        m += 8
    elif i % 128 == 0:
        m += 7
    elif i % 64 == 0:
        m += 6
    elif i % 32 == 0:
        m += 5
    elif i % 16 == 0:
        m += 4
    elif i % 8 == 0:
        m += 3
    elif i % 4 == 0:
        m += 2
    elif i % 2 == 0:
        m += 1

    if i % 125 == 0:
        n += 3
    elif i % 25 == 0:
        n += 2
    elif i % 5 == 0:
        n += 1

if m>=n:
    print(n)
else:
    print(m)