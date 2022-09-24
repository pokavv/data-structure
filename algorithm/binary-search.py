'''
이진탐색 Binary Search

- 탐색 전에 반드시 정렬되어야 함
- 살펴보는 범윌을 절반씩 죽여가면서 탐색
- 정렬 O(N*logN) + 이진탐색 O(logN) >> 결과적으로 O(N*logN)
- 미리 정렬되어 들어오면 이진탐색만 하면 되므로 O(logN)

선형탐색: O(N) vs 이진탐색: O(logN)
- 어떤 값을 찾기위해 탐색을 한번만 할땐 선형탐색이 유리
- 어떤 값을 찾기위해 탐색을 여러번 할땐 이진탐색이 유리
'''

from bisect import bisect_left, bisect_right

v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9)
three = bisect_right(v, 3) - bisect_left(v, 3)
four = bisect_right(v, 4) - bisect_left(v, 4)
six = bisect_right(v, 6) - bisect_left(v, 6)

print(f'num of 3: {three}') # 2
print(f'num of 4: {four}') # 0
print(f'num of 6: {six}') # 3