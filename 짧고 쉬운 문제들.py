#1152 단어 갯수 문제
import datetime
print(str(datetime.datetime.now())[:10])

#10699 날짜 문제
import datetime
print(str(datetime.datetime.now())[:10])

#1330 대소비교 문제
A, B = map(int,input().split())
if A>B:
	print(">")
elif A<B:
	print("<")
else:
	print("==")

#2438,2439 별 문제
N = int(input())
for i in range(N):
    i += 1
    K = N-i
    print(" " * K + "*" * i)

#2475 검증수 문제
print(sum([n**2 for n in map(int, input().split())]) % 10)