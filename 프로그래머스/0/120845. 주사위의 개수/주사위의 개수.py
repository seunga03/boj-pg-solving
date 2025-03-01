def solution(box, n):
    w = box[0] // n
    h = box[1] // n
    d = box[2] // n

    answer = w * h * d
    return answer