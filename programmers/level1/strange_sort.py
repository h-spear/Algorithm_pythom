# https://programmers.co.kr/learn/courses/30/lessons/12915/solution_groups?language=python3


def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x[0:]))
