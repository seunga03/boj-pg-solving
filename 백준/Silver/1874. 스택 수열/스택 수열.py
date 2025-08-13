N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())
    
stack = []
num = 1
answer = []
result = True

for i in range(N):
    x = A[i]
    if x >= num:
        while x >= num:
            stack.append(num)
            num += 1
            answer.append('+')
        stack.pop()
        answer.append('-')
    else:
        n = stack.pop()
        if x < n:
            print("NO")
            result = False
            break
        else:
            answer.append('-')
            
if result:
    for i in answer:
        print(i)