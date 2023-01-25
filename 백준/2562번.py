import sys

data = []
data2 = []

for i in range(9):
    a = int(sys.stdin.readline())
    data.append(a)
    data2.append(a)

data.sort()

print(data[8])

for i in range(9):
    if data[8] == data2[i]:
        print(i+1)
        break