# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    name_dicts = {name[i]: yearning[i] for i in range(len(name))}

    result = []
    for p in photo:
        score = 0
        for p_name in p:
            if p_name in name_dicts:
                score += name_dicts[p_name]
        result.append(score)
    return result