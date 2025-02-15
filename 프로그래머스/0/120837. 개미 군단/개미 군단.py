def solution(hp):
    answer = 0
    ant = [5, 3, 1]
    for damage in ant:
        answer += hp // damage
        hp %= damage
    return answer