# f(n) = f(n - 1) + f(n - 2)
import sys
input = sys.stdin.readline

cnt = 0
val = 10_007
arr = [0] * 1001
arr[1] = 1
arr[2] = 2

num = int(input())
for i in range(3, 1001):
    arr[i] = (arr[i - 1] + arr[i - 2]) % val
    cnt += 1

print(arr[num])
print(f'count : {cnt}')