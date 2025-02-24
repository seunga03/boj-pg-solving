'''
만약 참가자 수가 7명이고 a(김지민)와 b(임한수)가 각각 4, 7이라면 토너먼트는 아래와 같다.
a: 4 - 2 - 1 - 1    => a를 2로 나눈 값만큼 빼주는 식 이용
b: 7 - 4 - 2 - 1    => b를 2로 나눈 값만큼 빼주는 식 이용

         ___________결승__________
    _____1_____            _____2____
 __1__       __2__       __3__      4
1     2     3     4     5     6     7
'''

import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
count = 0

while a != b:
    a -= a // 2
    b -= b // 2
    count += 1
    
print(count)