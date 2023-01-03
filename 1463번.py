import sys

a = int(sys.stdin.readline())
data = [0,]

for i in range(a):
    if data[i] != 0:
        break
    data[i * 3]

print(data[a])