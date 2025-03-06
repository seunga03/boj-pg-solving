'''
에라토스테네스의 체: 값 x가 소수인지를 구하려면 x의 제곱근까지에 해당하는 숫자들로 나누어 보면 된다.
예) x = 16 
    x인 16의 약수는 [1, 2, 4, 8, 16]
    -> x의 제곱근인 4까지의 약수들로 x를 나누어보면 됨
        = 8과 16까지 확인할 필요가 없음
'''

import math

a, b = map(int, input().split())

for i in range(a, b+1):
    if i == 1:
        continue

    for j in range(2, int(math.sqrt(i))+1): # 에라토스테네스의 체
        if i % j == 0:
            break

    else:
        print(i)