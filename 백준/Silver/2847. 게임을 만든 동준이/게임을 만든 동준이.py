'''
입력값은 아래와 같다.
- n: 레벨의 수
- 리스트 scores: 각 레벨을 클리어하면 얻는 점수들

리스트 scores의 원소값 비교가 뒤->앞으로 진행되기 때문에 
반복문의 범위값들을 신경쓰며 코드를 작성해야 한다.

예를 들어 scores=[5, 3, 7, 5]라면
최종 scores는 [2, 3, 4, 5]가 되어야 한다.
'''
n = int(input())
scores = [int(input()) for _ in range(n)]

last_score = scores[-1]
count = 0

for i in range(n-2, -1, -1):
    if scores[i] >= scores[i+1]:
        val = scores[i] - (scores[i+1]-1)
        count += val
        scores[i] -= val
print(count)