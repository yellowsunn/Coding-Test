# https://school.programmers.co.kr/learn/courses/30/lessons/172928

move_row = [-1, 1, 0, 0]
move_col = [0, 0, -1, 1]
move_direction = {'N': 0, 'S': 1, 'W': 2, 'E': 3}


def solution(park, routes):
    start, end = find_start_axis(park)
    for route in routes:
        r_split = route.split()
        direct, count = r_split[0], int(r_split[1])
        start, end = move(park, start, end, move_direction[direct], count)

    return [start, end]


def move(park, start_row, start_col, idx, count):
    row, col = start_row, start_col
    for _ in range(count):
        next_row = row + move_row[idx]
        next_col = col + move_col[idx]
        if 0 <= next_row < len(park) and 0 <= next_col < len(park[0]) \
                and park[next_row][next_col] != 'X':
            row = next_row
            col = next_col
        else:
            return start_row, start_col
    return row, col


def find_start_axis(park):
    for row in range(len(park)):
        for col in range(len(park[0])):
            if park[row][col] == 'S':
                return row, col
    return 0, 0
