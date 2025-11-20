def solution(common):
    diff1 = common[1] - common[0]
    diff2 = common[-1] - common[-2]
    
    answer = 0
    
    if diff1 == diff2:
        # 등차
        answer = common[-1] + diff1
    else:
        # 등비
        answer = common[-1] * (common[1] // common[0])
        
    return answer