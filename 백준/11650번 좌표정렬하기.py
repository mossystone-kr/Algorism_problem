a = int(input())
b = []
for _ in range(a):
    b1, b2 = map(int, input().split())
    b.append([b1, b2])
b.sort()
for i in b:
    print(i[0], i[1])