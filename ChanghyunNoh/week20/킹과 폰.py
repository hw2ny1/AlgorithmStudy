import sys
input = sys.stdin.readline
from collections import deque
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]

N = int(input())
for tc in range(N):
    board = []
    for i in range(8):
        board.append(list(input().strip()))

    D = set()
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'D':
                D.add((i, j))
    K = deque()
    kx, ky = map(int, input().split())
    K.append((8 - ky, kx - 1))
    px, py = map(int, input().split())
    P = (8 - py, px - 1)
    answer = 'Black'
    while True:
        # 킹 이동: 현재까지의 킹 위치들이 모두 저장된 K 배열에서 8방향으로 이동시 가능한 위치를 모두 set(tmp)에 저장
        tmp = set()
        while K:
            now = K.pop()
            for d in range(8):
                ny, nx = now[0] + dy[d], now[1] + dx[d]
                if ny > 7 or ny < 0 or nx > 7 or nx < 0: continue
                if board[ny][nx] == 'D': continue
                if board[ny][nx] == 'F': continue
                if ny == P[0] + 1 and (nx == P[1] - 1 or nx == P[1] + 1): continue
                if ny == P[0] and nx == P[1]:
                    answer = 'White'
                    break
                tmp.add((ny, nx))
        # 폰 이동
        ny, nx = P[0] + 1, P[1]
        if P in tmp or (ny, nx) in tmp:
            answer = 'White'
            break
        if ny < 8 and board[ny][nx] == 'F':
            answer = 'White'
            break
        # 폰, 킹 초기화
        P = (P[0] + 1, P[1])
        K = list(tmp)
        # 폰이 끝에 도착시 종료
        if P[0] == 8:
            break
    print(answer)