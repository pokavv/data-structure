import sys
from bisect import bisect_right, bisect_left
input = sys.stdin.readline

n = int(input())
card = sorted(map(int, input().split()))
m = int(input())
qry = list(map(int, input().split()))
res = []

for i in qry:
    le = bisect_left(card, i)
    ri = bisect_right(card, i)
    res.append(1 if ri - le else 0)

print(*res)