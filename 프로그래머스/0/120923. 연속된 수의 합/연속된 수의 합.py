import math

def solution(num, total):
    answer = []
    start = int(total/num - (num-1)/2)
    for n in range(start, start + num):
        answer.append(n)
    
    return answer