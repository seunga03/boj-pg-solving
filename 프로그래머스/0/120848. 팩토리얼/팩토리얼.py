def solution(n):
    result, fact = 1, 1
    while fact <= n:
        result += 1
        fact *= result
    result -= 1
    return result