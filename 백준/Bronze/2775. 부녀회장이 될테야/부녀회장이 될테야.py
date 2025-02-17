'''
이 문제에서 만약 4층 3호의 값을 구하고 싶다면 과정은 아래와 같다.
4층 3호의 사람 수 = 4층 2호의 사람 수 + 3층 3호의 사람 수.
이를 식으로 표현하면 apt[i][j] = apt[i-1][j] + apt[i][j-1].
'''

t = int(input())        
for _ in range(t):
    k = int(input())    
    n = int(input())    
                        
    apt = [[0 for j in range(n)] for i in range(k+1)]

    for i in range(n):
        apt[0][i] = i+1
    for j in range(k+1):
        apt[j][0] = 1

    for i in range(1, k+1):
        for j in range(1, n):
            apt[i][j] = apt[i-1][j] + apt[i][j-1]

    print(apt[k][n-1])