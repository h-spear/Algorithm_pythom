# https://school.programmers.co.kr/learn/courses/30/lessons/120887


def solution(i, j, k):
    answer = 0
    for _i in range(i, j + 1):
        answer += str(_i).count(str(k))
    return answer
