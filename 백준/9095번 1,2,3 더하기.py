import sys

a = int(sys.stdin.readline())
num = []
data = []

for _ in range(a):
    num.append(int(sys.stdin.readline()))

for _ in range(15): data.append(0)

data[1] = 1
data[2] = 1
data[3] = 1

for i in range(1,12):
    data[i + 1] = data[i] + data[i + 1]
    data[i + 2] = data[i] + data[i + 2]
    data[i + 3] = data[i] + data[i + 3]

for k in num:
    print(data[k])

"""
더 간단한 풀이가 있다.
어짜피 범위가 10까지니까
그냥 규칙 찾아서 다 더해버려도 문제 없다.
-----------------------------------

T = int(input())

def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else :
        return sol(n-1) + sol(n-2) + sol(n-3)

for i in range(T):
    n = int(input())
    print(sol(n))


"""