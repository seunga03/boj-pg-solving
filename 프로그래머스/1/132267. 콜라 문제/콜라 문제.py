def solution(a, b, n):
    answer = 0
    remainder = 0

    while n >= a:
        remainder = n % a
        exchanged = n // a
        n = exchanged * b + remainder
        answer += exchanged * b

    return answer