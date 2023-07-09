'''
흰색, 빨간색, 파란색 함수를 각각 만들었음
말 하나씩 이동하고 K번째 말까지 옮겼으면 턴 += 1
4개 이상인 곳이 있다면 바로 break

문제에 주어진 그대로 쭉 구현하다보니
뭔가 중복인 부분이 많이 보여서 아쉬운데
일단 제출...
'''

def white(ci, cj, ni, nj):
    while mal[ci][cj]:
        mal[ni][nj].append(mal[ci][cj].pop(0))

def red(ci, cj, ni, nj):
    while mal[ci][cj]:
        mal[ni][nj].append(mal[ci][cj].pop())

def blue(ci, cj, dir):
    mal[ci][cj][0][1] = dirchange[dir]
    ni, nj = ci + di[dirchange[dir] - 1], cj + dj[dirchange[dir] - 1]
    if 0 <= ni < N and 0 <= nj < N:
        if board[ni][nj] == 0:
            white(ci, cj, ni, nj)
        elif board[ni][nj] == 1:
            red(ci, cj, ni, nj)

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
mal = [[[] for _ in range(N)] for _ in range(N)]
for k in range(K):
    i, j, d = map(int, input().split())
    mal[i - 1][j - 1].append([k + 1, d])
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
dirchange = {1:2, 2:1, 3:4, 4:3}
turn = 1
cnt = 1
ans = -1
while turn <= 1000:
    # 말 찾기
    ci, cj, dir = -1, -1, -1
    for i in range(N):
        for j in range(N):
            if mal[i][j] and mal[i][j][0][0] == cnt:
                ci, cj = i, j
                dir = mal[i][j][0][1]

    # 색깔에 따라 말 이동하기
    if ci != -1 and cj != -1:
        ni, nj = ci + di[dir - 1], cj + dj[dir - 1]
        # 안쪽 영역
        if 0 <= ni < N and 0 <= nj < N:
            # 흰색
            if board[ni][nj] == 0:
                white(ci, cj, ni, nj)
            # 빨간색
            elif board[ni][nj] == 1:
                red(ci, cj, ni, nj)
            # 파란색
            else:
                blue(ci, cj, dir)
        # 바깥쪽 영역
        else:
            blue(ci, cj, dir)

        # 네 개 이상인 곳이 있는지 확인하기
        for i in range(N):
            for j in range(N):
                if len(mal[i][j]) >= 4:
                    ans = turn
                    break
    if ans != -1:
        break

    # K번째 말까지 다 이동시켰으면 턴 늘리기
    if cnt == K:
        turn += 1
        cnt = 1
    else:
        cnt += 1
print(ans)