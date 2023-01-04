import sys

a = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
data.sort()
sum = 0

for i in range(len(data)+1):
    for j in range(i):
        sum += data[j]

print(sum)