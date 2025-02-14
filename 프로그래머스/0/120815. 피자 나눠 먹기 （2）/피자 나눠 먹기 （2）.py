def solution(n):
    remain = 0
    count = 1

    while True:
        if (6 + remain) % n != 0:
            remain = (6 + remain) % n
            count += 1
        else:
            return count            
