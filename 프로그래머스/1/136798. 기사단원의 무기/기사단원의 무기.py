def solution(number, limit, power):
    answer = 0
    count_list = []
    
    for i in range(1, number + 1):
        if count_divisors(i) <= limit:
            count_list.append(count_divisors(i))
        else:
            count_list.append(power)   
    return sum(count_list)

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
                
    return count