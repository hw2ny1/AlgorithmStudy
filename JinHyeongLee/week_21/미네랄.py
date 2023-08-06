'''
아직 못 품
1. throw_height 짝수 index는 왼쪽에서 오른쪽, 홀수 index는 오른쪽에서 왼쪽으로 미네랄 여부 탐색
2. 미네랄('x') 발견 시 그 자리 파괴('.'으로 변환)
2-1. 파괴 후 4방향 델타 탐색하여 미네랄 존재 여부 확인하여 있으면 덱(is_mineral)에 추가
3. is_mineral에 있는 좌표들로 위에서 떨어질 수 있는 분리된 클러스터 찾기
3-1. 분리된 클러스터가 있다면 얼만큼 떨어져야 하는지 탐색 후 떨어뜨리기
    -> 여기서 어떻게 해야할 지 모르겠음
4. 이 후 던지는 횟수만큼 진행
'''

import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    visited = [[0 for _ in range(C)] for _ in range(R)]
    visited[i][j] = 1
    cluster = []
    while queue:
        i, j = queue.popleft()
        if i == R - 1:  # 맨 꼭대기면 바로 종료
            return
        if cave[i + 1][j] == '.':  # 파괴된 미네랄 바로 밑이 비어있으면 cluster 리스트에 좌표 추가
            cluster.append([i, j])
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 3, 6, 9, 12시 방향 순서
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C:
                if cave[ni][nj] == 'x' and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    queue.append([ni, nj])

    return

R, C = map(int, input().split())
cave = [list(str(input().rstrip())) for _ in range(R)]
N = int(input())
throw_height = list(map(int, input().split()))
is_mineral = deque()

for i in range(N):
    T = R - throw_height[i]
    # 번갈아가며 미네랄 파괴
    if i % 2:  # 홀수 index
        for j in range(C):
            if cave[T][j] == 'x':
                cave[T][j] = '.'
                break

    else:  # 짝수 index
        for j in range(C - 1, -1, -1):
            if cave[T][j] == 'x':
                cave[T][j] = '.'
                break

    # 파괴 후 4방향 델타 탐색으로 미네랄 여부 확인
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C and cave[ni][nj] == 'x':
            is_mineral.append([ni, nj])

    
    while is_mineral:
        x, y = is_mineral.popleft()
        bfs(x, y)

for c in cave:
    print(''.join(c))