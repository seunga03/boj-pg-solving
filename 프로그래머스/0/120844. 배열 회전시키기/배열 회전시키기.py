def solution(numbers, direction):
    if direction == "right":
        answer = [numbers[-1]] + numbers[:-1]
    elif direction == "left":
        answer = numbers[1:] + [numbers[0]]
    return answer