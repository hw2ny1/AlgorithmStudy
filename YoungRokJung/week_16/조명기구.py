# 도저히 아이디어가 떠오르지 않아요
# 모든 경우의 수를 따지는거밖에 생각이 안나는데 그럼 무조건 시간초과....
# 열, 행 몇번 교환 됐는지 visited으로 체크하면서 백트래킹으로 구현하는 방법 밖에는 생각이 안남
# 밑 코드도 변환하는 과정만 구현해놓고 아이디어 떠오르지 않아서 미해결..
import sys,copy
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
c_visited = [[0]*m for _ in range(n)]
r_visited = [0]*n
comb = []
for i in range(n):
    for j in range(m):
        if i != j :
            comb.append((i,j))
print(comb)
final = [list(map(int,input().split())) for _ in range(n)]
print(graph,final)
checking = 0

def r_btn(i,graph,lst): # i행 색상 변경
    global checking, final

    if graph == final or checking :
        checking = 1
        return lst

    temp = copy.deepcopy(graph)
    for j in range(len(temp[i])) :
        if temp[i][j] == 0 :
            temp[i][j] = 1
        else :
            temp[i][j] = 0

    return 0

def c_btn(i,j,graph,lst): # i,j 열 교환
    global checking, final

    if graph == final or checking :
        checking = 1
        return lst

    temp = copy.deepcopy(graph)
    temp[i],temp[j] = temp[j],temp[i]

    return 0




