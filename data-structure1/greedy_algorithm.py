#################
# 매 순간마다 최선의 경우만을 골라감
# 다른 경우는 고렿지 않고 나중을 생각하지 않음
# 모든 경우를 다 보지않으니 완전탐색보다 빠름
# 어떤 경우가 최선인지 찾는게 포인트 > 규칙성을 찾아야함
#################

# 동전 거스름돈 문제 1
# 10, 50, 100, 500원 동전들을 무한하게 갖고있을때 손님에게 800원을 거슬러주려할때 동전을 최소한으로 주는 방법은?
# 답: 500원 1개, 100원 3개 (최대한 큰 값의 동전으로 최대한 준 뒤 점점 값을 줄여나감) > 규칙성

# 동전 거스름돈 문제 2
# 100, 400, 500원 동전들을 무한하게 갖고있을때 손님에게 800원을 거슬러주려할때 동전을 최소한으로 주는 방법은?
# 답: 400원 2개 (문제 1의 규칙성이 깨짐(500원 1개 100원 3개), 500원이 배수관계X > Greedy Algorithm에 적합x)

# Greedy Algorithm은 반례가 존재하지않아야 쓰기에 적합함

#############################

# boj 11047 : Ai는 Ai-1의 배수라는 조건을 가짐 > Greedy 가능

num, k = map(int, input().split())
coin = []
res = 0

for _ in range(num):
    coin.append(int(input()))
coin.reverse()

for i in coin:
    res += k // i
    k %= i
    
    # 값 확인
    print(f'coin: {i}, k: {k}, res: {res}')

print(res)
print()
# boj 1449 : 

hole, leng = map(int, input().split())
pipe = [False] * 1001 # 크기 1001짜리 pipe list 생성하고 모두 False로 채움

for i in map(int, input().split()):
    pipe[i] = True # pipe[입력값]인 위치에만 True
    
x = 0 # 현재 좌표
res = 0 # 테이프 사용횟수
while x < 1001:
    if pipe[x]:
        res += 1 # 테이프 하나 사용
        x += leng # 테이프 붙이기(length = tape length)
    else:
        x += 1

print(res)