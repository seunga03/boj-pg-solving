def solution(array):
    count = [0] * (max(array) + 1)
    
    for i in array:
        count[i] += 1
        
    mode = 0
    for j in count:
        if j == max(count):
            mode += 1
    return -1 if mode > 1 else count.index(max(count))