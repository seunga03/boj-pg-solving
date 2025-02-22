import sys
input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes.sort(reverse=True)
answers = [ropes[i] * (i+1) for i in range(n)]

print(max(answers))