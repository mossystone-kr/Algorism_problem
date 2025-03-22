N, M = map(int,(input().split()))

d = list(map(int, input().split())) # 카드 리스트

result = 0
Max = 0

for i in range(N-2): # 3중 for문을 돌면서 겹치지 않게 범위를 지정
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if d[i]+d[j]+d[k] > M: # 3개의 값 더한것이 M보다 크다면 넘어감
                continue
            else:
                result = d[i]+d[j]+d[k]
                if Max <= result: # M과 가장 유사한 값은 가장 큰값이기 때문에 비교해서 큰값을 저장
                    Max = result

print(Max)

n = int(input())
cnt = 0
result=666
while True:
    if'666'in str(result):
        cnt+=1
        if cnt==n:break
    result+=1
print(result)