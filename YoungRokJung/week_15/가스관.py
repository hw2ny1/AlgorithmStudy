# 1. 일단 그래프 값에 따라 이동 방향이 모두 다르므로 딕셔너리로 좌표를 짜야한다고 생각해서 point_dic 구성
# 2. 그래프를 따라가다가 파이프는 연결되어 있는데 그래프 값이 '.' 인 곳이 해커가 해킹한 블록
# 3. 그 블록에서 가스가 들어오고 나갈수 있는 방향을 조사한 뒤 그 값이 point_dic의 value 값이랑 같으면 그 블록의 파이프는 point_dic의 key값

import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
point_dic = {'|' : [[-1,0],[1,0]], '-' : [[0,1],[0,-1]], '+' : [[-1,0],[0,1],[1,0],[0,-1]], '1' : [[0,1],[1,0]], '2' : [[-1,0],[0,1]], '3' : [[-1,0],[0,-1]], '4' : [[1,0],[0,-1]]}
point = [[-1,0],[0,1],[1,0],[0,-1]]
check = []
point_check = []

def BFS(i,j) :
    global check

    visited[i][j] = 1
    q = deque()
    q.append((i,j))

    while q :
        r,c = q.popleft()

        for di,dj in point_dic[graph[r][c]] :
            ni,nj = r+di, c+dj
            if 0<=ni<R and 0<=nj<C and visited[ni][nj] == 0 :
                if graph[ni][nj] == '.' : # 해커가 해킹한 블록
                    check.append((ni,nj))
                    continue

                elif graph[ni][nj] == 'Z' or graph[ni][nj] == 'M' :
                    visited[ni][nj] = 1
                    continue

                q.append((ni,nj))
                visited[ni][nj] = 1

def final_check(i,j) : # 해킹한 블록에서 4방향을 조사해 가스가 들어오고 나갈 수 있는 방향이라면 point_check에 넣어줌
    global point_check
    pc = []
    for di,dj in point :
        ni,nj = i+di, j+dj
        if 0<=ni<R and 0<=nj<C and graph[ni][nj] != '.'  :
            if graph[ni][nj] != 'Z' and graph[ni][nj] != 'M' :
                if [i-ni, j-nj] in point_dic[graph[ni][nj]] :
                    point_check.append([di,dj])

for i in range(R):
    for j in range(C):
        # 좌표값이 M이거나 Z일 때 한번만 BFS 돌리면 되므로 확인용으로 temp 사용
        temp = 0
        if graph[i][j] == 'M' or graph[i][j] == 'Z' :
            temp = 1
            visited[i][j] = 1 # M 이거나 Z일 때 방문처리
            for di,dj in point : # M 이나 Z에 연결된 파이프에서부터 BFS 돌려야하므로 4방향 조사
                ni,nj = i+di, j+dj
                if 0<=ni<R and 0<=nj<C and graph[ni][nj] != 'Z' and graph[ni][nj] != 'M' and graph[ni][nj] != '.' :
                    visited[ni][nj] = 1
                    BFS(ni,nj)
                    break
            break

    if temp :
        final_check(check[0][0],check[0][1]) # 해킹한 블록에서 4방향 조사
        for key,value in point_dic.items() :
            if point_check == value : # 들어오고 나갈 수 있는 방향이 value 값이랑 같으면 해킹당한 블럭은 key
                print(check[0][0]+1,check[0][1]+1,key)
        break
