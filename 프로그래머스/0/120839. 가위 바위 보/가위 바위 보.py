def solution(rsp):
    answer = ''
    dic = {"0": "5", "2": "0", "5": "2"}
    for i in rsp:
        if i in dic: # `i`가 딕셔너리의 키인지 확인
            answer += dic[i]
    return answer