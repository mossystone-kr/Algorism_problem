"""
a = int(input())
target = []
stack = [1]
now = 0
k = 2
ans = ["+"]
for i in range(a):
    target.append(int(input()))
while len(target):
    print(target[now], stack[-1])
    if target[now]>stack[-1]:
        ans += "+"
        stack.append(k)
        k += 1
    elif target[now]==stack[-1]:
        ans += "-"
        now += 1
        stack.pop()
        target.pop()
    elif target[now]<stack[-1]:
        print("NO")
        exit(0)
for d in ans:
    print(d)
"""
count = 1
temp = True
stack = []
op = []

N = int(input())
for i in range(N):
    num = int(input())
    # num이하 숫자까지 스택에 넣기
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        temp = False
        break

# 스택 수열을 만들수 있는지 여부에 따라 출력
if temp == False:
    print("NO")
else:
    for i in op:
        print(i)