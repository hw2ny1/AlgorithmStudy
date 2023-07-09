import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[-1]*N for _ in range(N)]    # 방문 처리 -1로 초기화
point = [[0,1],[1,0],[0,-1],[-1,0]]     # 델타

viruses = []    # 바이러스 정보 저장할 리스트
for i in range(N):
    for j in range(N):
        if graph[i][j] :
            viruses.append((graph[i][j],i,j)) # 바이러스 번호, 좌표 위치 저장
            visited[i][j] = 0   # 0으로 방문 초기화

S,X,Y = map(int,input().split()) # 주어진 시간, 조사해야할 좌표
viruses.sort()  # 작은 번호부터 전염되므로 바이러스 번호 순서로 오름차순 정렬
q = deque(viruses)

while q:
    num, i, j = q.popleft()

    if visited[i][j] == S : # visited[i][j] == S일 때 S+1인 곳은 조사할 필요 없으므로 continue
        continue

    for di,dj in point :    # 일반적인 bfs
        ni,nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N and graph[ni][nj] == 0 and visited[ni][nj] == -1 :
            graph[ni][nj] = num
            visited[ni][nj] = visited[i][j] + 1
            q.append((graph[ni][nj],ni,nj))


if graph[X-1][Y-1] :
# 문제는 0,0이 1,1부터 시작이라 -1씩 해주고 조사, x-1,y-1좌표에 바이러스가 있으면 번호 출력
    print(graph[X-1][Y-1])
else :
    print(0)