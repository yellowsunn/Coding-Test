# https://school.programmers.co.kr/learn/courses/30/lessons/172927

INF = 10 ** 9

fatigue = [
    [1, 1, 1],
    [5, 1, 1],
    [25, 5, 1]
]

mineral_dict = {"diamond": 0, "iron": 1, "stone": 2}


def solution(picks, minerals):
    result = INF
    for i in range(3):
        result = min(recursive(picks, minerals, i, 0), result)
    return result


def recursive(picks, minerals, pick_idx, mineral_idx):
    if sum(picks) == 0:
        return 0
    if picks[pick_idx] <= 0:
        return INF

    total = 0
    picks[pick_idx] -= 1
    for i in range(mineral_idx, min(mineral_idx + 5, len(minerals))):
        m = mineral_dict[minerals[i]]
        total += fatigue[pick_idx][m]

    if mineral_idx + 5 < len(minerals):
        count = INF
        for i in range(3):
            count = min(recursive(picks, minerals, i, mineral_idx + 5), count)
        total += count
    picks[pick_idx] += 1

    return total

print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))