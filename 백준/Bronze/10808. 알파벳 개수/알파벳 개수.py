s = input()
answer = [0] * 26

for i in s:
    answer[ord(i) - 97] += 1

for i in answer:
    print(i, end=" ")