s = input().split('-')
num = []

for i in s:
    if '+' in i:
        num.append(sum(map(int, i.split('+'))))
    else:
        num.append(int(i))
        
answer = num[0]
for minusNumber in num[1:]:
    answer -= minusNumber
    
print(answer)