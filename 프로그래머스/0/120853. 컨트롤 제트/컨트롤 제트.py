def solution(s):
    arr = s.split(' ')
    stack = []
    answer = 0
    
    for a in arr:
        if a != "Z":
            stack.append(a)
        else:
            stack.pop()
            
    for s in stack:
        answer += int(s)
    return answer