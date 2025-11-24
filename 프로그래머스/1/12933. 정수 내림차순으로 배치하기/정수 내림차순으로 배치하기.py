def solution(n):
    answer = 0
    s = sorted(str(n)) [::-1]
    return int("".join(map(str, s)))
