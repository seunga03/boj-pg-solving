import sys
input = sys.stdin.readline

l = [int(input()) for _ in range(9)]
l.sort()
sub = sum(l) - 100

found = False
for i in range(9):
    for j in range(i + 1, 9):
        if l[i] + l[j] == sub:
            del l[j]
            del l[i]
            found = True
            break
    if found:
        break

print(*l, sep="\n")