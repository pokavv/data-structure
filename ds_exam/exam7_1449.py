hole, leng = map(int, input().split())
pipe = [False] * 1001 # 크기 1001짜리 pipe list 생성하고 모두 False로 채움

for i in map(int, input().split()):
    pipe[i] = True # pipe[입력값]인 위치에만 True
    
x = 0 # 현재 좌표
use = 0 # 테이프 사용횟수
while x < 1001:
    if pipe[x]:
        use += 1 # 테이프 하나 사용
        x += leng # 테이프 붙이기(length = tape length)
    else:
        x += 1

print(use)