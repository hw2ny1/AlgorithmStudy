from collections import deque

"""
문　제　2931_가스관
메모리　34476 KB
시　간　68 ms

지운 블록이 빈 칸이 되었으므로 시작점과 끝점에서 출발하여 길이 끝나는 지점의 빈칸을 각각 구한다.
그리고 그 빈칸의 교집합이 바로 지워진 블럭이 된다.
그 블럭의 경우 문자에 대한 델타 좌표와 일치하는 key값을 찾아 출력하였다.
"""

# 문자에 대한 델타 좌표
view = {
    '.':[],
    '|':[(1, 0), (-1, 0)],
    '-':[(0, 1), (0, -1)],
    '+':[(1, 0), (-1, 0), (0, 1), (0, -1)],
    '1':[(1, 0), (0, 1)],
    '2':[(-1, 0), (0, 1)],
    '3':[(-1, 0), (0, -1)],
    '4':[(1, 0), (0, -1)]
}

# M과 Z에서 시작해서 경로가 끝나는 곳을 set에 담에서 return한다.
def search(x,y):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    dq = deque()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] != '.':
                dq.append((nx,ny))
                visited[nx][ny] = 1
    visited[x][y] = 1
    temp = set()

    while dq:
        x, y = dq.popleft()
        if arr[x][y] == '|':
            for ddx, ddy in view['|']:
                nx = x + ddx
                ny = y + ddy
                if nx < 0 or nx >= N or ny < 0 or ny >= M:continue
                if visited[nx][ny]:continue
                visited[nx][ny] = 1
                if arr[nx][ny] == '.':
                    temp.add((nx,ny))
                else:
                    dq.append((nx,ny))
        elif arr[x][y] == '-':
            for ddx, ddy in view['-']:
                nx = x + ddx
                ny = y + ddy
                if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
                if visited[nx][ny]: continue
                visited[nx][ny] = 1
                if arr[nx][ny] == '.':
                    temp.add((nx, ny))
                else:
                    dq.append((nx, ny))
        elif arr[x][y] == '+':
            for ddx, ddy in view['+']:
                nx = x + ddx
                ny = y + ddy
                if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
                if visited[nx][ny]: continue
                visited[nx][ny] = 1
                if arr[nx][ny] == '.':
                    temp.add((nx, ny))
                else:
                    dq.append((nx, ny))
        elif arr[x][y] == '1':
            for ddx, ddy in view['1']:
                nx = x + ddx
                ny = y + ddy
                if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
                if visited[nx][ny]: continue
                visited[nx][ny] = 1
                if arr[nx][ny] == '.':
                    temp.add((nx, ny))
                else:
                    dq.append((nx, ny))
        elif arr[x][y] == '2':
            for ddx, ddy in view['2']:
                nx = x + ddx
                ny = y + ddy
                if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
                if visited[nx][ny]: continue
                visited[nx][ny] = 1
                if arr[nx][ny] == '.':
                    temp.add((nx, ny))
                else:
                    dq.append((nx, ny))
        elif arr[x][y] == '3':
            for ddx, ddy in view['3']:
                nx = x + ddx
                ny = y + ddy
                if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
                if visited[nx][ny]: continue
                visited[nx][ny] = 1
                if arr[nx][ny] == '.':
                    temp.add((nx, ny))
                else:
                    dq.append((nx, ny))
        elif arr[x][y] == '4':
            for ddx, ddy in view['4']:
                nx = x + ddx
                ny = y + ddy
                if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
                if visited[nx][ny]: continue
                visited[nx][ny] = 1
                if arr[nx][ny] == '.':
                    temp.add((nx, ny))
                else:
                    dq.append((nx, ny))
    return temp


dx = [1,-1,0,0]
dy = [0,0,1,-1]
N,M=map(int,input().split())
arr = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'M':
            temp1 = search(i,j)
        elif arr[i][j] == 'Z':
            temp2 = search(i,j)

# 두 set의 교집합, 즉 파이프가 사라져서 빈공간이 겹치는곳에 연결하면 된다.
temp = temp1&temp2
let = []
# 경우의 수가 여러개 일수 도 있으니 반복문으로 순회하며 확인
for x, y in temp:
    for tx, ty in view['+']:
        nx = x + tx
        ny = y + ty
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if arr[nx][ny] not in view.keys():continue
        if (-tx, -ty) in view[arr[nx][ny]]:
            let.append((tx, ty))
    # 정답을 찾으면 방향에 맞는 문자 출력
    for key, value in view.items():
        if value == let:
            print(x+1, y+1, key)
            exit(0)



