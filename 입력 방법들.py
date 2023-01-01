import sys

#입력 1개
a = int(sys.stdin.readline())

#입력 3개
b,c,d = map(int,sys.stdin.readline().split())

#입력 리스트
data = list(map(int,sys.stdin.readline().split()))

#입력 2차원 리스트
data2 = []
n = int(sys.stdin.readline())
for i in range(n):
    data2.append(list(map(int,sys.stdin.readline().split())))

#문자열 리스트
#예시
    #입력
    #3
    #안녕안녕
    #나는 지수야
    #헬륨가스 마셨더니 이렇게됐지

    #출력
    #['안녕안녕', '나는 지수야', '헬륨가스 마셨더니 이렇게됐지']

n = int(sys.stdin.readline())
data3 = [sys.stdin.readline().strip() for i in range(n)]