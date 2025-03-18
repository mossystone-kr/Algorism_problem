a, b = map(int, input().split())
c = 0
while True:
    c += a
    a = a//b
    if a == 0:
        break
print(c)
