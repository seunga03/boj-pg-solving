def solution(quiz):
    answer = []
    
    for q in quiz:
        compare = q.split(" = ")
        expression = compare[0].split(" ")
        if expression[1] == "+" and int(expression[0]) + int(expression[2]) == int(compare[1]):
            answer.append("O")
        elif expression[1] == "-" and int(expression[0]) - int(expression[2]) == int(compare[1]):
            answer.append("O")
        else:
            answer.append("X")

    return answer