#############
# Key와 Value로 구성
# C++에선 red-black tree (삽입/삭제 O(log N))
# Python에선 Hash로 구성(삽입/삭제 O(1))
#############

m = {}
m['Yoon'] = 40
m['Moon'] = 100
m['Joe'] = 50
print('size: ', len(m))

for key in m:
    print(key, m[key]) # key와 value print