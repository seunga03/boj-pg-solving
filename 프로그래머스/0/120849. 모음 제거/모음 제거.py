def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for s in my_string:
        if s not in vowel:
            answer += s
    return answer