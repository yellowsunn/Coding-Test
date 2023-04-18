# https://school.programmers.co.kr/learn/courses/30/lessons/181188?language=python3
# 백준 회의실 배정 (https://www.acmicpc.net/problem/1931) 과 동일한 문제

def solution(targets):
    targets.sort(key=lambda x: (x[1], x[0]))
    start = 0
    count = 0
    for target in targets:
        if start <= target[0]:
            count += 1
            start = target[1]
    return count
