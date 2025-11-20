def solution(array, n):
    answer = 0
    distance = []
    
    for a in array:
        distance.append(max(a, n) - min(a, n))
    
    mindis = distance[0]
    index = 0
    
    for i in range(len(distance)):
        if mindis > distance[i]:
            mindis = distance[i]
            index = i
        elif mindis == distance[i]:
            if array[i] < array[index]:
                index = i
    
    return array[index]