n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
answer = ((sum(scores) / m) * 100) / n
print(answer)