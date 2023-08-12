import sys
input = sys.stdin.readline
from collections import deque

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

R, C = map(int, input().split())
cave = []
for i in range(R):
    cave.append(list(input().strip()))
N = int(input())
heights = list(map(int, input().split()))
for i in range(N):
    heights[i] -= 1

def throw(height, direction):
    # y, x 초깃값 설정
    y, x = -1, -1

    # 방향에 따라 탐색해서 크리스탈 위치 찾기
    if direction == 1:
        for i in range(C):
            if cave[height][i] == 'x':
                y, x = height, i
                break
    else:
        for i in range(C - 1, -1, -1):
            if cave[height][i] == 'x':
                y, x = height, i
                break

    # 허공에 던졌으면 return
    if y + x == -2:
        return

    # 파괴 후 추락
    cave[y][x] = '.'
    if height < R - 1 and cave[height - 1][x] == 'x' and cave[y] == ['.' for _ in range(C)]:
        fall()
    return

def fall():
    global cave
    global cnt
    q = deque()
    visited = [[False] * C for _ in range(R)]
    minimum = 101
    for i in range(R):
        for j in range(C):
            if cave[i][j] == 'x':
                q.append((i, j))
                visited[i][j] = True
                break

    while q:
        now = q.popleft()
        for d in range(4):
            ny, nx = now[0] + dy[d], now[1] + dx[d]
            if ny < 0 or ny > R - 1 or nx < 0 or nx > C - 1: continue
            if visited[ny][nx]: continue
            if cave[ny][nx] == 'x':
                visited[ny][nx] = True
                if ny < minimum:
                    minimum = ny
                q.append((ny, nx))
    return

direction = -1
for height in heights:
    direction *= -1
    throw(height, direction)

for i in cave:
    for j in i:
        print(j, end='')
    print()
