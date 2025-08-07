import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()
cnt = 0

for x in range(n):
    find = A[x]
    i = 0
    j = n - 1
    while i < j:
        if A[i] + A[j] == find:
            if i != x and j != x:
                cnt += 1
                break
            elif i == x:
                i += 1
            elif j == x:
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1
        
print(cnt)