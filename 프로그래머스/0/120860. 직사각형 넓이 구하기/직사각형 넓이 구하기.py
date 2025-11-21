def solution(dots):
    answer = 0

    xlist = []
    ylist = []
    
    for x, y in dots:
        xlist.append(x)
        ylist.append(y)
    
    return (max(xlist) - min(xlist)) * (max(ylist) - min(ylist))