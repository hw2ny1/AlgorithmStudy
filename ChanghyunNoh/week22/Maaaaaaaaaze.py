# 아직 디버깅중..

from itertools import combinations_with_replacement
from collections import deque
import sys
input = sys.stdin.readline

dz = [0, 0, 0, 0, -1, 1]
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]

maze = [[] for _ in range(5)]
for i in range(5):
    for j in range(5):
        maze[i].append(list(map(int, input().split())))

def rotate(lst):
    new_lst = []
    for i in range(5):
        new_lst.append([lst[j][i] for j in range(4, -1, -1)])
    return new_lst

def bfs():
    if maze[0][0][0] == 0: return -1
    if maze[4][4][4] == 0: return -1
    q = deque()
    q.append((0, 0, 0))
    visited = [[[-1] * 5 for _ in range(5)] for __ in range(5)]
    visited[0][0][0] = 0
    while q:
        now = q.popleft()
        z, y, x = now[0], now[1], now[2]
        for d in range(6):
            nz, ny, nx = z + dz[d], y + dy[d], x + dx[d]
            if nz < 0 or nz > 4 or ny < 0 or ny > 4 or nx < 0 or nx > 4: continue
            if visited[nz][ny][nx] >= 0: continue
            if maze_temp[nz][ny][nx] == 0: continue
            visited[nz][ny][nx] = visited[z][y][x] + 1
            if nz == ny == nx == 4: return visited[nz][ny][nx]
            q.append((nz, ny, nx))
    return visited[4][4][4]

answer = 1000
combs = list(combinations_with_replacement([i for i in range(1, 5)], 5))
for comb in combs:
    maze_temp = maze[:]
    for i in range(5):
        for j in range(comb[i]):
            maze_temp[i] = rotate(maze_temp[i])
    result = bfs()
    from pprint import pprint
    pprint(maze_temp)
    if result != -1:
        answer = min(answer, result)
if answer == 1000:
    answer = -1
print(answer)