import sys

a,b = map(int,sys.stdin.readline().split())
list = [0]*100001
list[a] = 1
confirmed = [a]
confirmed1 =[]

while list[b] == 0:
    for i in confirmed:
        if 2*i < 100001 and (list[2*i] > list[i] + 1 or list[2*i] == 0):
            list[2*i] = list[i] + 1
            confirmed1.append(2*i)
        if i+1 < 100001 and (list[i+1] > list[i] + 1 or list[i+1] == 0):
            list[i+1] = list[i] + 1
            confirmed1.append(i+1)
        if i-1 >0 and (list[i-1] > list[i] + 1 or list[i-1] == 0):
            list[i-1] = list[i] + 1
            confirmed1.append(i-1)
    confirmed.clear()
    confirmed = confirmed1.copy()
    confirmed1.clear()

k = list[b]-1
print(k)