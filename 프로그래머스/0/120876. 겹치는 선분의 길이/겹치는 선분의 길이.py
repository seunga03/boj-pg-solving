def solution(lines):
    left = min(line[0] for line in lines)
    right = max(line[1] for line in lines)

    offset = -left
    check = [0] * (right - left)

    for s, e in lines:
        for i in range(s + offset, e + offset):
            check[i] += 1

    return sum(1 for x in check if x >= 2)
