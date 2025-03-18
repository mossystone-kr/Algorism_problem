a, b, c = map(int, input().split("-"))
d = int(input())

c += d
while c>30:
    b += 1
    c -= 30
while b>12:
    a += 1
    b -= 12
if c<10:
    c = '0'+str(c)
if b<10:
    b = '0'+str(b)

print(str(a)+"-"+str(b)+"-"+str(c))