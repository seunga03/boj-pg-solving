def solution(order):
    answer = 0
    game369 = "369"
    for i in str(order):
        if i in game369:
            answer += 1
    return answer