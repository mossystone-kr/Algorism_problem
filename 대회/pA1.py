import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

val = b in a

if val:
    print("O")
else:
    print("X")