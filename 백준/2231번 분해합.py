a = int(input())
ans = 0
for i in range(1000000):
    b = 0
    for j in str(i):
        b += int(j)
    if i + b == a:
        ans = i
        break
print(ans)