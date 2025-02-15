def solution(s1, s2):
    answer = 0
    
    for s in range(len(s1)):
        if s1[s] in s2:
            answer += 1
            
    return answer