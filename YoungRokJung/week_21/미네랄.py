import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(r)]
point = [[0,1],[1,0],[0,-1],[-1,0]]

n = int(input())
# 땅에 붙어있는 미네랄에서 출발해서 클러스터를 이루고있는 미네랄들 파악
def mineralState() :
    visited = [[0]*c for _ in range(r)]
    for j in range(c):
        if graph[r-1][j] == 'x' and visited[r-1][j] == 0 :
            visited[r-1][j] = 1
            q = deque()
            q.append((r-1,j))
            while q :
                y,x = q.popleft()

                for dy,dx in point :
                    ny,nx = y+dy, x+dx
                    if not (0<=ny<r and 0<=nx<c) : continue
                    if graph[ny][nx] == 'x' and visited[ny][nx] == 0 :
                        q.append((ny,nx))
                        visited[ny][nx] = 1
    return visited

# 떨어질 거리 측정
def fallingDistance(fall,graph) :
    distance = 1
    while True :
        for y,x in fall :
            if y+distance == r-1 : # 끝에 도착하거나
                return distance
            if graph[y+distance+1][x] == 'x' : # 중간에 미네랄을 만났을 때
                return distance
        distance += 1

def moveMinerals(y,x) :
    ms = mineralState()

    group = [] # 클러스터 이루고 있는 좌표들
    fall = [] # 표면 좌표 ( 떨어질 수 있는 미네랄 )

    for dy,dx in point :
        ny,nx = y+dy, x+dx
        if not (0<=ny<r and 0<=nx<c) : continue

        if graph[ny][nx] == 'x' and ms[ny][nx] == 0 :
            q = deque()
            q.append((ny,nx))
            ms[ny][nx] = 2
            graph[ny][nx] = '.'
            group.append((ny,nx))

            while q :
                i,j = q.popleft()

                if graph[i+1][j] == '.' :
                    fall.append((i,j))

                for di,dj in point :
                    ni,nj = i+di, j+dj
                    if not (0<=ni<r and 0<=nj<c) : continue
                    if graph[ni][nj] == 'x' and ms[ni][nj] == 0 :
                        ms[ni][nj] = 2
                        group.append((ni,nj))
                        q.append((ni,nj))
                        graph[ni][nj] = '.'

    if fall :
        d = fallingDistance(fall,graph)
        for i,j in group :
            graph[i+d][j] = 'x'

lst = list(map(int,input().split()))
for i in range(n) :
    lst[i] = r - lst[i]

for i in range(len(lst)) :
    h = lst[i]
    if i%2 == 0 : # 왼쪽에서 오른쪽
        for j in range(c) :
            if graph[h][j] == 'x' :
                graph[h][j] = '.'
                moveMinerals(h,j)
                break

    elif i%2 == 1 : # 오른쪽에서 왼쪽
        for j in range(c-1,-1,-1) :
            if graph[h][j] == 'x' :
                graph[h][j] = '.'
                moveMinerals(h,j)
                break

for i in range(r):
    print(''.join(graph[i]))