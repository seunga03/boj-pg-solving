'''
입력값은 다음과 같다. 
- n: 대여소 개수
- 리스트 a: 각 대여소의 수정 완료된 자전거의 개수
- 리스트 b: 각 대여소의 수정 전의 자전거의 개수

새로운 리스트 tmp를 생성하고 반복문으로 [리스트 b의 원소값 - 리스트 a의 원소값]을 담아준다.
예를 들어, a = [1, 1, 5]이고, b = [4, 2, 1]이라면 tmp = [3, 1, -4]

리스트 tmp의 원소들 중 양수인 값들의 합이 결국 구하고자 하는 값이므로, 
조건문을 통해 양수값들의 합을 구한다.
만약 tmp = [3, 1, -4]라면, 출력되어야 하는 값은 4.
'''

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

tmp = [b[i]-a[i] for i in range(n)]
answer = 0

for x in tmp:
    if x > 0:
        answer += x

print(answer)