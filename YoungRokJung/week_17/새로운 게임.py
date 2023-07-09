import sys
input = sys.stdin.readline

n,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
point = [[0,1],[0,-1],[-1,0],[1,0]]
chess_graph = [[[] for _ in range(n)] for _ in range(n)] # 체스 좌표에 어떤 체스말들이 있는지 저장할 리스트
chess_info = [0]*k  # 체스 번호를 인덱스로한 체스말의 정보를 저장할 리스트 (행,열,방향)

def move(num):
    i,j,d = chess_info[num]
    if num != chess_graph[i][j][0] : # 현재 번호가 그 좌표의 가장 아래 말의 번호가 아니라면 바로 리턴
        return False

    ni,nj = i + point[d][0], j + point[d][1]
    if ni < 0 or ni>=n or nj <0 or nj>=n or graph[ni][nj] == 2 : # 좌표를 벗어나거나 만나게되는 칸이 파란칸이라면
        if d == 0 or d == 2 :
            nd = d+1
        else :
            nd = d-1
        chess_info[num][2] = nd # 방향 바꿔주고 한번 더 조사
        ni,nj = i + point[nd][0], j + point[nd][1]
        if ni < 0 or ni >= n or nj < 0 or nj >= n or graph[ni][nj] == 2:
            return False

    if graph[ni][nj] == 1 : # 빨간 칸을 만난다면 그 좌표칸에 쌓여있는 말들 거꾸로 뒤집어주기
        chess_graph[i][j].reverse()

    for m in chess_graph[i][j] :
        chess_graph[ni][nj].append(m) # 이동한 칸으로 전부 쌓아주기
        chess_info[m][0], chess_info[m][1] = ni,nj # 체스말의 정보 갱신 (행,열) -> 방향은 그대로

    chess_graph[i][j] = [] # 이동하고 난 후 원래 있던 좌표 초기화
    if len(chess_graph[ni][nj]) >= 4 : # 이동한 좌표에 쌓여있는 말이 4개 이상이라면 리턴
        return True
    return False


for i in range(k):
    y,x,d = map(int,input().split())
    chess_graph[y-1][x-1].append(i) # 1,1부터 시작이라 -1씩 , 방향도 마찬가지
    chess_info[i] = [y-1,x-1,d-1]

cnt = 0
while cnt < 1000: # 1000번 이상이거나 무한히 끝나지 않으면 -1 출력 조건
    cnt += 1
    for i in range(k): #
        if move(i) :
            print(cnt)
            exit()
print(-1)