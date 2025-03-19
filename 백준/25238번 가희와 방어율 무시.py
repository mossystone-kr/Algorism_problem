a, b = map(int, input().split())
b2 = 100 - b
a2 = a/100*b2
if a2<100:
    print(1)
else:
    print(0)
