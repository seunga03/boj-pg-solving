def solution(s):
    s = s.lower()
    answer = False
    p_count, y_count = 0, 0
    for x in s:
        if x == 'p':
            p_count += 1
        if x == 'y':
            y_count += 1
    if p_count == y_count:
        answer = True
    return answer