# itertools.combinations 활용 (brute-force)

import sys
import itertools

dwarf_list = []
for i in range(9):
    dwarf_list.append(int(sys.stdin.readline()))

for i in itertools.combinations(dwarf_list, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break # 답 한가지만을 출력해야되기 때문에 답을 찾으면 break문 삽입해서 반복문을 벗어난다.
    
####################################################

# itertools.combinations 활용 x

dwarf_list2 = [int(sys.stdin.readline()) for i in range(9)]
height_sum = sum(dwarf_list2)
dwarf_list2.sort()

for i in range(8):
    for j in range(i + 1, 9):
        if height_sum - dwarf_list2[i] - dwarf_list2[j] == 100:
            for v in range(9):
                if i != v and j != v:
                    print(dwarf_list2[v])
            exit()