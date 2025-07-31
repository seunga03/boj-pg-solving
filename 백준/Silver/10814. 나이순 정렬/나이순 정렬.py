n = int(input())
l = []

for i in range(n):
    age, name = input().split()
    l.append([int(age), i, name])
    
l.sort()
    
for a, b, c in l:
    print(a, c)