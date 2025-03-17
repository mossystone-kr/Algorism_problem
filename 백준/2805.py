import sys

"""
num, need = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))

def ans_check(cut):
    res = 0
    for i in range(num):
        if trees[i] >= cut:
            res = res + trees[i] - cut
    return res
    
def binary_search(target, start, end):
    mid = (start + end) // 2
    
    if ans_check(mid) == target:
        print(mid)
    elif ans_check(mid) < target:
        binary_search(target, start, mid-1)
    elif ans_check(mid) > target:
        binary_search(target, mid+1, end)

binary_search(need, 0, max(trees))
"""

from collections import Counter

n, m = map(int, sys.stdin.readline().split())
trees = Counter(map(int, sys.stdin.read().split()))

s = 1
e = 1000000000

while s <= e:
    mid = (s + e) // 2
    tot = sum((h - mid) * i for h, i in trees.items() if h > mid)

    if tot >= m:
        s = mid + 1
    elif tot < m:
        e = mid - 1

print(e)