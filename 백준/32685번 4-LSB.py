password = []
lastpass = ""
for _ in range(3):
    password.append(int(input()))
for i in password:
    a = bin(i)[2:]
    while len(a)<4:
        a = "0" + a
    lastpass = lastpass + a[-4:]
ans = str(int(lastpass,2))
while len(ans)<4:
    ans = "0" + ans
print(ans)
