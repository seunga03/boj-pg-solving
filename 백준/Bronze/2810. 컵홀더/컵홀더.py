n = int(input())
seats = input()

cupholder = n + 1 - seats.count('LL')
print(min(n, cupholder))