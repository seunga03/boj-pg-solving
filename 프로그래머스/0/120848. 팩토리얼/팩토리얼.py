import math

def solution(n):
    for i in range(1, 11):
        if n > math.factorial(i):
            continue
        elif n == math.factorial(i):
            return i
        else:
            return i-1