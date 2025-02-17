import math
f = math.factorial

def solution(balls, share):
    answer = f(balls) // (f(balls-share) * f(share))
    return answer