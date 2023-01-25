import sys
a,b = map(int, sys.stdin.readline().split())

if b<45:
    if a==0:
        b += 60
        b -= 45
        print("23 " + str(b))
    else:
        b += 60
        b -= 45
        a -= 1
        print(str(a) + " " + str(b))
else:
    b -=45
    print(str(a)+" "+str(b))