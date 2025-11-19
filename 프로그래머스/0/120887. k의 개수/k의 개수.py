def solution(i, j, k):
    answer = 0
    s = ""

    for x in range(i, j+1):
        s += str(x)        
    
    return s.count(str(k))