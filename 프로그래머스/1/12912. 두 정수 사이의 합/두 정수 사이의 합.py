def solution(a, b):
    answer = 0
    mx = max(a, b) + 1
    mn = min(a, b)
    for i in range(mn, mx):
        answer += i
    return answer