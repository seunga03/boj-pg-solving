N = list(input())

for i in range(len(N)):
    Max = i
    for j in range(i + 1, len(N)):
        if N[j] > N[Max]:
            Max = j
    if N[i] < N[Max]:
        temp = N[i]
        N[i] = N[Max]
        N[Max] = temp

for i in range(len(N)):
    print(N[i], end='')