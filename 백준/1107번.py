import sys

objective = int(sys.stdin.readline())
bug = int(sys.stdin.readline())
bug_button = list(map(int,sys.stdin.readline().split()))

now = 100
button_press = 0

if bug == 9:
    button_press = objective - now
else:
