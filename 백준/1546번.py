import sys

a = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
data.sort()

for i in range(a):
    data[i] = data[i] / data[a-1] * 100

sum = 0

for i in range(a):
    sum += data[i]

print(sum/a)