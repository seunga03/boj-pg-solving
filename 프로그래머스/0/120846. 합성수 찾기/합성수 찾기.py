import math

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if is_composite(i):
            answer += 1
    return answer

def is_composite(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            cnt += 2
    if n // int(math.sqrt(n)) == int(math.sqrt(n)):
        cnt -= 1
    if cnt >= 3:
        return True
    return False