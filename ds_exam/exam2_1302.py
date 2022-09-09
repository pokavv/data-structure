import sys

dic = dict()
for i in range(int(sys.stdin.readline())):
    title = input()
    if title in dic:
        dic[title] += 1
    else:
        dic[title] = 1

best = max(dic.values())
sort_list = []

for k, v in dic.items():
    if v == best:
        sort_list.append(k)

sort_list.sort()
print(sort_list[0])