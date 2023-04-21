# https://school.programmers.co.kr/learn/courses/30/lessons/169199

from collections import deque

move_row = [0, -1, 0, 1]
move_col = [1, 0, -1, 0]
row_size, col_size = 0, 0


def solution(board):
    global row_size
    global col_size
    row_size, col_size = len(board), len(board[0])

    start_row, start_col = find_start_axis(board)
    return bfs(board, start_row, start_col)


def find_start_axis(board):
    for row in range(row_size):
        for col in range(col_size):
            if board[row][col] == 'R':
                return row, col
    return -1, -1


def bfs(board, start_row, start_col):
    q = deque()
    visited = [[False for _ in range(col_size)] for _ in range(row_size)]
    q.append((start_row, start_col, 0))
    visited[start_row][start_col] = True

    while q:
        row, col, dist = q.popleft()
        if board[row][col] == 'G':
            return dist
        for i in range(4):
            next_row, next_col = move(board, row, col, i)
            if (next_row != row or next_col != col) and not visited[next_row][next_col]:
                q.append((next_row, next_col, dist + 1))
                visited[next_row][next_col] = True
    return -1


def move(board, row, col, direction):
    next_row, next_col = row, col
    while True:
        r = next_row + move_row[direction]
        c = next_col + move_col[direction]
        if 0 <= r < row_size and 0 <= c < col_size and board[r][c] != 'D':
            next_row, next_col = r, c
        else:
            return next_row, next_col
