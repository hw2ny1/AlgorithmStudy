import sys
input = sys.stdin.readline

def getMovingWarning(x,y,stops) : # 움직이는 위험 좌표 구하기, x,y 에 pawn 좌표
    mw = []
    if y+1<8 :
        if (x-1>=0 and (y+1,x-1) not in stops) :
            mw.append((y+1,x-1))
        if (x+1 < 8 and (y+1,x+1) not in stops) :
            mw.append((y+1,x+1))
    return mw


def move(xk,yk,xp,yp,warnings,stops) :
    white = False

    movingWarnings = getMovingWarning(xp,yp,stops) # 움직이는 위험 좌표
    banList = warnings + stops + movingWarnings # 킹이 갈 수 없는 좌표
    canMove = [] # 킹이 이동할 수 있는 좌표
    for di,dj in king :
        ni,nj = yk+di, xk+dj
        if 0<=ni<8 and 0<=nj<8 and (ni,nj) not in banList :
            canMove.append((ni,nj))

    if not canMove : return white # canMove가 없으면 return False

    for y,x in canMove :
        # 조건 1. 킹이 폰을 직접 잡을 경우
        if yp == y and xp == x :
            white = True

        # 조건 2. pawn의 다음 위치가 F 이거나, 킹이 있는 위치일 경우
        if ((yp+1,xp) in stops) or (yp+1 == y and xp == x) :
            white = True

        if white : break # 킹이 이긴 경우 break

        else :
            if yp + 1 == 8 : # 폰이 끝 점에 도달한 경우
                continue
            # 킹이 이동한 좌표, 폰이 한 칸 아래로 이동한 좌표 넣어서 다시 탐색
            white = move(x,y,xp,yp+1,warnings,stops)

    return white

T = int(input())
king = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
# 금지 둘다 x, 위험 폰만, 폰 왼,오른 아래 위험 칸
for _ in range(T):
    graph = [list(input().rstrip()) for _ in range(8)]

    warnings = [] # D 좌표
    stops = [] # F 좌표

    for i in range(8):
        for j in range(8):
            if graph[i][j] == 'D' : warnings.append((i,j))
            elif graph[i][j] == 'F' : stops.append((i,j))

    # 행,열 주의 !
    xk,yk = map(int,input().split())
    xp,yp = map(int,input().split())
    xk -= 1; yk=8-yk; xp-=1; yp=8-yp;

    result = move(xk,yk,xp,yp,warnings,stops)
    if result : print("White")
    else : print("Black")



