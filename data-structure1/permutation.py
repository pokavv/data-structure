###########################
# 모든 경우의 수를 순서대로 살펴볼때 용이하다
# 삼성에서 next_permutation 활용문제 다수 출제
# 순서 존재
###########################

from itertools import permutations
v = [0, 1, 2, 3]

for i in permutations(v, 4):
    print(i)