'''
입력값은 아래와 같다.
- n: 사람의 수
- 리스트 p: 각 사람이 돈을 인출하는데 걸리는 시간

각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하려면
p는 오름차순으로 정렬되어 있다는 전제가 있어야 한다. 

따라서 answer(필요한 시간의 합의 최솟값)은 아래와 같다.
answer = (p[0] * n) + (p[1] * (n-1)) + ... + (p[n-1] * 1)
'''
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

p.sort()
answer = 0

for i in range(n):
    answer += p[i] * (n-i)
    
print(answer)