def solution(x):
    answer = True
    s = str(x)
    sum_of_digits = 0
    
    for i in s:
        sum_of_digits += int(i)
    
    if x % sum_of_digits != 0:
        answer = False
    return answer