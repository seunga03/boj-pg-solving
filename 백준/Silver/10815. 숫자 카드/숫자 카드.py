n = int(input())
cards1 = set(map(int, input().split()))
m = int(input())
cards2 = list(map(int, input().split()))

result = [1 if i in cards1 else 0 for i in cards2]
        
print(*result)