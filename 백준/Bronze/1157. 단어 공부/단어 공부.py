word = input().upper()
cnt = [0] * 26

for i in word:
    cnt[ord(i) - 65] += 1
    
if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(chr(cnt.index(max(cnt)) + 65))