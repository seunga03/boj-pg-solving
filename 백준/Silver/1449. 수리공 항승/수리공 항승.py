'''
for문을 돌면서 확인할 것: 누수 부분이 테이프 영역에 포함되는지 여부
포함 -> count의 값이 변화 없어야
포함x -> count의 값 1 증가, start의 값도 해당 자리로 리셋 (테이프를 새로 붙여주는 작업)
'''

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
leaks = list(map(int, input().split()))
leaks.sort()

start = leaks[0] 
count = 1

for i in leaks[1:]:
    if i in range(start, start+l):
        continue
    else:
        count += 1
        start = i

print(count)