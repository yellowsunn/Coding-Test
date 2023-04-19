# https://school.programmers.co.kr/learn/courses/30/lessons/178870

INF = 10 ** 9


def solution(sequence, k):
    result_len = INF

    total = 0
    end = 0
    result = []
    for start in range(len(sequence)):
        while total < k and end < len(sequence):
            total += sequence[end]
            end += 1

        if total == k and end - start < result_len:
            result = [start, end - 1]
            result_len = end - start

        total -= sequence[start]
    return result
