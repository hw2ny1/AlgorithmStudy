import sys
input = sys.stdin.readline

"""
문　제　9114_킹과_폰
메모리　31256 KB
시　간　1416 ms

참고해서 풀었습니다
"""


def get(x, y, F):
    temp = []
    if 0 < y-1 :
        if (0 < x-1) and ((x-1, y-1) not in F) :
            temp.append((x-1, y-1))
        if (x+1 < 9) and ((x+1, y-1) not in F) :
            temp.append((x+1, y-1))
    return temp

def simulate(kx, ky, px, py, D, F):
    white = False

    List = []

    ret = get(px, py, F)
    banList = D + F + ret

    for i in [-1,0,1]:
        for j in [-1,0,1]:
            ny = ky + i
            nx = kx + j
            if ny < 1 or ny > 8 or nx < 1 or nx > 8: continue
            if not i and not j: continue
            if (nx, ny) not in banList: List.append((nx, ny))

    if len(List) == 0 : return white

    for (x, y) in List:
        # 승리조건 1
        if x == px and y == py : white = True

        # 승리조건 2
        if ((px, py - 1) in F) or (px == x and py - 1 == y) : white = True
        
        # 승리했으면 끝
        if white: break
        else :
            if py > 1:
                white = simulate(x, y, px, py-1, D, F)
    return white

N = int(input())
for _ in range(N):
    D = []
    F = []
    for i in range(8):
        line = input()
        for j, ch in enumerate(line) :
            if ch == 'D' :
                D.append((j+1, 8-i))
            elif ch == 'F' :
                F.append((j+1, 8-i))

    kx, ky = map(int, input().split()) # white
    px, py = map(int, input().split()) # black

    # 시뮬
    result = simulate(kx, ky, px, py, D, F)
    if result: print("White")
    else: print("Black")