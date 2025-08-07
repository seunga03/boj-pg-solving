n = int(input())
m = int(input())
ids = list(map(int, input().split()))
ids.sort()
start_index = 0
end_index = n-1
cnt = 0

while start_index < end_index:
    if ids[start_index] + ids[end_index] < m:
        start_index += 1
    elif ids[start_index] + ids[end_index] > m:
        end_index -= 1
    else:
        cnt += 1
        start_index += 1
        end_index -= 1
        
print(cnt)