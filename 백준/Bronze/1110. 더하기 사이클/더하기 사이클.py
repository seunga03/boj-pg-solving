n = int(input())

if n >= 10:
    original = str(n)
else:
    original = "0" + str(n)

new = original
count = 0

while True:
    count += 1
    next = new[-1] + str((int(new[0]) + int(new[1])) % 10)
    if original == next:
        break
    new = next

print(count)
