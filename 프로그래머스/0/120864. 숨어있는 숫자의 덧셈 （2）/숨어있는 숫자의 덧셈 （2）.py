def solution(my_string):
    answer = 0
    tmpNum = ""
    for s in my_string:
        if s.isdigit():
            tmpNum += s
        else:
            if tmpNum:
                answer += int(tmpNum)   
                tmpNum = "" 
                
    if tmpNum:
        answer += int(tmpNum)   

    return answer