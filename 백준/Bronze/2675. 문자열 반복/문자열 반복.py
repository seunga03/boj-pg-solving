t = int(input())
for _ in range(t):
    s = input().split()
    r = int(s[0])
    text = s[1]
    result = ''
    
    for ch in text:
        result += ch * r
    print(result)