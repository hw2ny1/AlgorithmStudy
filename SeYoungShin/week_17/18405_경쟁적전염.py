'''
stack에 (시간, 바이러스 종류, i좌표, j좌표)를 넣고 sort
이후 BFS 

pop(0) 여기서 시간이 더 걸리지 않았나 생각중
(deque()를 쓰자니 sort가 안되어서 걍 리스트 씀)
'''

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
stack = []
for i in range(N):
    for j in range(N):
        if info[i][j]:
            stack.append((0, info[i][j], i, j))
stack.sort()
while stack:
    t, num, ci, cj = stack.pop(0)
    if t == S:
        break
    for k in range(4):
        ni, nj = ci + di[k], cj + dj[k]
        if 0 <= ni < N and 0 <= nj < N and not info[ni][nj]:
            info[ni][nj] = num
            stack.append((t + 1, info[ni][nj], ni, nj))
print(info[X - 1][Y - 1])