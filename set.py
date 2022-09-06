################
# 중복허용 X
# 삽입/삭제: O(1) (C++에선 O(log N))
################

s = set()

# 값 add
s.add(123)
s.add(456)
s.add(789)
s.add(123)
s.add(456)
s.add(321)

# 값 pop : 무엇이 빠질지 모름
s.pop()

# 값 remove
s.remove(321)

'''
# 값 clear : 모든 요소 제거
s.clear()
'''

print('size: ', len(s))

for i in s:
    print(i)