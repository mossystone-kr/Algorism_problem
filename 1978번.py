import sys

a = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
b=0

for i in range(a+1):
    k = int(data[i]**(1/2))
    sum = 0
    for j in range(1, k+1):
        if (data[i] % j) != 0:
            sum += 1
    if sum == 0:
        b += 1
        print(data[i])
print(b)