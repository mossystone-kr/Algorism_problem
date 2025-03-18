a, b = map(int, input().split())
c = a*b
if c%2 == 0:
    print(int(c/2))
else:
    print(str(c//2)+".5")
