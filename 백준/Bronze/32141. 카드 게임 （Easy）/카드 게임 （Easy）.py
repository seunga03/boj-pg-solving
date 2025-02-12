n, h = map(int, input().split())
d = list(map(int, input().split()))

total_damage = 0
answer = 0

for x in d:
    total_damage += x
    answer += 1
    
    if total_damage >= h:
        print(answer)
        break
    
else:
    print(-1)
    