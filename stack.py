##############
# 삽입/삭제: O(1)
# LIFO (Last In First Out)
##############

st = []

st.append(123)
st.append(456)
st.append(789)
print('size: ', len(st))

while len(st) > 0:
    print(st[-1])
    st.pop()