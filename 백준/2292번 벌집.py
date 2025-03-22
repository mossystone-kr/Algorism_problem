"""
i = int(input())
ans = 1
st = 0
end = 1
while True:
    if st < i <= end:
        break
    ans += 1
    st = end + 1
    end = end + (ans-1)*6
print(ans)
"""
num = int(input())
numbox = 1
cnt = 1

while num > numbox:
    numbox += 6 * cnt
    cnt += 1
print(cnt)