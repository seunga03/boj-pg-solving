word = input().upper()
l = list(set(word))
tmp = [0] * len(l)

for i in word:
    for j in range(len(l)):
        if i == l[j]:
            tmp[j] += 1

cnt = 0

for k in tmp:
    if max(tmp) == k:
        cnt += 1

if cnt == 1:
    print(l[tmp.index(max(tmp))])
else:
    print("?")