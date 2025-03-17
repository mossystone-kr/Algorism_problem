import sys

n = int(input())
list1 = list(map(int, sys.stdin.readline().split()))
arr = sorted(set(list1))

dic = {arr[i]:i for i in range(len(arr))}

for i in list1:
    print(dic[i],end=" ")
