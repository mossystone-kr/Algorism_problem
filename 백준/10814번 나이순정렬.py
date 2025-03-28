a = int(input())
b = []
for _ in range(a):
    b1, b2 = input().split()
    b.append([int(b1), b2])
b.sort(key=lambda x:x[0])
for i in b:
    print(i[0], i[1])