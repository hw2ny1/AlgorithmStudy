import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
tmp = [[0, 0], [0, 0]]
now = 0
for i in range(N):
    d, m, r = map(int, input().split())
    if d == now:
        if tmp[d][0] + m > M:
            now = 1 - d
            tmp[d][0] = m
            print(tmp[d][1], tmp[d][1] + T)
        else:
            tmp[d][0] += m
        tmp[d][1] = r
    else:
        if r >= tmp[1-d][1] + T * 2:
            now = 1 - d
            tmp[1-d][0] = 0
            print(tmp[1-d][1], tmp[1-d][1] + T)
        if tmp[d][0] + m > M:
            now = 1 - d
            tmp[d][0] = m
            print(tmp[d][1], tmp[d][1] + T)