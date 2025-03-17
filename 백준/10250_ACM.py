n = int(input())
field = [[int(x) for x in input().split()] for i in range(n)]
for i in range(n):
    e = field[i][2] % field[i][0]
    f = field[i][2] // field[i][0] + 1
    if e == 0:
        f -= 1
        e = field[i][0]
    print(e*100+f)

"""
원래는 일케 했었음.
하지만 이렇게 하니까 사람%층 했을때 0이 되버리는 경우가 있어서 곤란함.
그니까 5층에 10명이 오면
0층 3호에 가게 되는데
실제로는 5층 2호로 가야하니까
예외때문에 수정을 해줘야한다.
왜 이걸 생각못했지?

++ 추가로 출력값은 저렇게 하면 된다. 오랜만에 풀어서인지 다 까먹음 ㅎㅎ..

n = int(input())
field = [[int(x) for x in input().split()] for i in range(n)]
for i in range(n):
    e = field[i][2] % field[i][0]
    f = field[i][2] // field[i][0] + 1
    if len(str(f))==1:
        f = '0'+str(f)
    print(str(e)+str(f))
"""