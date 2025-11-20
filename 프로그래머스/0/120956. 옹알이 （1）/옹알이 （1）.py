def solution(babbling):

    answer = []
    words = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for word in words:
            i = i.replace(word, " ")
        
        answer.append(i.replace(" ", ""))
        
    return answer.count("")