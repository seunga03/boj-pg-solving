def solution(bin1, bin2):
    carry = 0
    i = len(bin1) - 1
    j = len(bin2) - 1
    result = []

    while i >= 0 or j >= 0 or carry:
        digit1 = int(bin1[i]) if i >= 0 else 0
        digit2 = int(bin2[j]) if j >= 0 else 0

        total = digit1 + digit2 + carry

        result.append(str(total % 2))
        carry = total // 2
        
        i -= 1
        j -= 1

    return ''.join(reversed(result))
