S, P = map(int, input().split())
DNA = list(input())
ACGT = list(map(int, input().split()))
checklist = [0] * 4
answer = 0


# 조건에 충족하는지 확인하는 함수
def is_vaild():
    global answer
    for i in range(4):
        if checklist[i] < ACGT[i]:
            break
    else:
        answer += 1


# 맨처음 최소 개수 체크
for i in DNA[:P]:
    if i == 'A':
        checklist[0] += 1
    elif i == 'C':
        checklist[1] += 1
    elif i == 'G':
        checklist[2] += 1
    elif i == 'T':
        checklist[3] += 1

# 첫 번째 부분 문자열이 충족하는지 확인
is_vaild()

# 슬라이딩 윈도우 관련 인덱스 초기화
out_index = 0
in_index = P

while in_index < S:
    if DNA[in_index] == 'A':
        checklist[0] += 1
    elif DNA[in_index] == 'C':
        checklist[1] += 1
    elif DNA[in_index] == 'G':
        checklist[2] += 1
    elif DNA[in_index] == 'T':
        checklist[3] += 1

    if DNA[out_index] == 'A':
        checklist[0] -= 1
    elif DNA[out_index] == 'C':
        checklist[1] -= 1
    elif DNA[out_index] == 'G':
        checklist[2] -= 1
    elif DNA[out_index] == 'T':
        checklist[3] -= 1

    is_vaild()

    in_index += 1
    out_index += 1

print(answer)