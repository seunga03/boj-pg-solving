a, b = map(int, input().split())
c, d = map(int, input().split())

l = [a, b, c, d]
answers = []

for i in range(4):
    answers.append((l[0]/l[2]) + (l[1]/l[3]))
    l = [l[2], l[0], l[3], l[1]]

print(answers.index(max(answers)))