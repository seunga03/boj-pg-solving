def solution(emergency):
    answer = []
    sortedArr = sorted(emergency, reverse=True)
    for i in range(len(emergency)):
        answer.append(sortedArr.index(emergency[i])+1)
    return answer