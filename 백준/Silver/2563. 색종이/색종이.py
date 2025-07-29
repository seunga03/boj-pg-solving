paper = [[False] * 100 for _ in range(100)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[j][i] = True
            
answer = sum(row.count(True) for row in paper)
print(answer)