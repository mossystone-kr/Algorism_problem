import sys

a = int(sys.stdin.readline())
data = [0,0,0,0,0,0,0,0,0,0]

for l in range(a+1):
    data.append(0)


for i in range(a+1):
    if data[i] != 0:
        break
    data[i * 3] += 1
    data[i * 2] += 1
    data[i + 1] += 1
    print(data[i])

print(data[a+1])