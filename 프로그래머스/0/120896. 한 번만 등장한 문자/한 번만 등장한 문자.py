def solution(s):
    count = {}
    answer = ''

    for x in s:
        count[x] = count.get(x, 0) + 1
    
    sortlist = sorted(count.keys())

    for x in sortlist:
        if count[x] == 1:
            answer += x

    return answer