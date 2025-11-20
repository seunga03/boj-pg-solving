def solution(s):
    answer, cnt_x, cnt_other = 0, 0, 0
    x = ""

    for a in s:
        if cnt_x == 0 and cnt_other == 0:
            x = a
        if a == x:
            cnt_x += 1
        else:
            cnt_other += 1

        if cnt_x == cnt_other:
            answer += 1
            cnt_x, cnt_other = 0, 0

    if cnt_x != cnt_other:
        answer += 1

    return answer