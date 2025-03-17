stairs = []
n = int(input())
dp = [0]*n
for i in range(n):
	stairs.append(int(input()))

if n<=2:
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[1] + stairs[0]
    dp[2] = max(stairs[1]+stairs[2], stairs[0]+stairs[2])
    for i in range(3, n):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    print(dp[-1])