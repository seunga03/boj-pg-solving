def solution(array):
    array.sort()
    odd = len(array) // 2 
    answer = array[odd]
    return answer