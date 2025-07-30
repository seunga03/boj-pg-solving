n = int(input())
xys = [tuple(map(int, input().split())) for _ in range(n)]
xys.sort()
for x, y in xys:
    print(x, y)