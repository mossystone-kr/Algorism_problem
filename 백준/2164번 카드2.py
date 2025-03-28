"""a = list(range(1, int(input())+1))
while len(a) != 1:
    a.pop(0)
    a.append(a.pop(0))
print(a[0])"""
input = int(input())
square = 2

while True:
    if (input == 1 or input == 2):
        print(input)
        break
    square *= 2
    if (square >= input):
        print((input - (square // 2)) * 2)
        break