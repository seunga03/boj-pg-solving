def solution(sides):

    possible = []
    
    for x in range(1, sides[0] + sides[1]):
        if x == max(x, sides[0], sides[1]):
            possible.append(x)
            
    
    for x in range(1, max(sides) + 1):
        if x + min(sides) > max(sides) and x not in possible:
            possible.append(x)
    
    print(possible)
    return len(possible)