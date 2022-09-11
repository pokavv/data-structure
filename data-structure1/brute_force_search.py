##########################################
# 브루트포스 Brute-force (무차별대입)
# 가장 확실한 방법이라 많이 쓰임
# n개의 수를 입력받아 두 수를 뽑아 합이 가장 클 때는? 브루트포스
# 모든 경우의 수: nC2 (n*(n-1) / 2*1) >> 이중 for문 사용, but 수가 너무 커지면 시간초과발생
##########################################

def bruteforce(arr, n):
    nlist = []
    if n == 1:
        for i in arr:
            nlist.append([i])
    else:
        for i in range(len(arr) - n + 1):
            for j in bruteforce(arr[i + 1:], n - 1):
                nlist.append([arr[i]] + j)
    print(len(nlist))
    return nlist

print(bruteforce([4, 5, 7, 8, 9, 6, 3, 1], 2))