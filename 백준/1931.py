import sys

def meeting_room(times):
    times.sort(key=lambda x: (x[1], x[0]))
    end = 0
    a = 0
    for i, j in times:
        if end <= i:
            a += 1
            end = j
    return a

n = int(sys.stdin.readline().strip())
times = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    times.append((x, y))

print(meeting_room(times))