import sys

a = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
data.sort()
print(str(data[0]) + " " + str(data[a-1]))