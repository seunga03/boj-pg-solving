n = int(input())
b = list(map(int, input().split()))
count = 0

for i in range(n-2):
    if b[i] == 1:
        count += 1
        b[i] = 0
        b[i+1], b[i+2] = 1 - b[i+1], 1 - b[i+2]

# 마지막 두 개의 버튼 확인
if b[-2] == 1:
    count += 1
    b[-2] = 0
    b[-1] = 1 - b[-1]

if b[-1] == 1:
    count += 1
    b[-1] = 0

print(count)
