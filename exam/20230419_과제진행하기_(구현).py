# https://school.programmers.co.kr/learn/courses/30/lessons/176962

from collections import deque


def solution(plans):
    q = deque(sorted(plans, key=lambda x: x[1]))

    stop_jobs = []
    current_job = None
    finished_jobs = []
    for i in range(24 * 60 * 100):
        if current_job and current_job[1] > 0:
            current_job = (current_job[0], current_job[1] - 1)

        if current_job and current_job[1] == 0:
            finished_jobs.append(current_job[0])
            current_job = stop_jobs.pop() if stop_jobs else None

        if q:
            hour, minute = map(int, q[0][1].split(":"))
            time = hour * 60 + minute
            if time == i:
                name, _, left_time = q.popleft()
                if current_job:
                    stop_jobs.append(current_job)
                current_job = (name, int(left_time))
    return finished_jobs