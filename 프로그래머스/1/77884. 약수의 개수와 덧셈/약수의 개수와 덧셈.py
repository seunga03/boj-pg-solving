import math

def solution(left, right):
    answer = 0
    for x in range(left, right+1):
        if count_divisors_efficient(x) % 2 == 0:
            answer += x
        else:
            answer -= x
    return answer

def count_divisors_efficient(n):
    count = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            if i * i != n:
                count += 2
            else:
                count += 1
    return count
