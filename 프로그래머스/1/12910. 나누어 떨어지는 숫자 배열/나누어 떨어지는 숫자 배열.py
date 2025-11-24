def solution(arr, divisor):
    answer = [a for a in arr if a % divisor == 0]
    if answer == []:
        answer.append(-1)
    return sorted(answer)