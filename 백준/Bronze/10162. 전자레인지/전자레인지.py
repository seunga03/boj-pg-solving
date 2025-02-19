t = int(input())
abc = [300, 60, 10]
answer = []

for i in abc:
    answer.append(t // i)
    t %= i

if t == 0:
    print(answer[0], answer[1], answer[2])
else:
    print(-1)
