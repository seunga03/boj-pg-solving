'''
여러 예제를 손으로 적어보았을 때 (커플석(LL)의 개수 - 1)만큼의 사람이 컵을 컵홀더에 놓을 수 없었다.
이 원리로 코드를 짜보려 한다.
'''

n = int(input())
seats = input()

l = seats.count("LL")
if l >= 2:
    print(n - l + 1)
else:
    print(n)