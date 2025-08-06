import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0]
tmp = 0

for i in A:
    tmp += i
    S.append(tmp)
    
for i in range(m):
    s, e = map(int, input().split())
    print(S[e] - S[s-1])