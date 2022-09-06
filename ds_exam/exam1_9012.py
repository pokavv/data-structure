import sys

for _ in range(int(sys.stdin.readline())):
    st = []
    isVPS = True

    for i in input():
        if i == '(':
            st.append(i)
        else:
            if len(st) > 0:
                st.pop()
            else:
                isVPS = False
                break
    
    if len(st) > 0:
        isVPS = False
    
    print('YES' if isVPS else 'NO')