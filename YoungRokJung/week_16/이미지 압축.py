# boj 1992 문제를 활용하고 다른 코드도 좀 참고해서 풀었습니다.
# 괄호가 열릴 때 루트노드가 하나씩 생성
# 1. 루트노드와 자식노드들의 합, 중복되는 루트노드는 제거해주고 루트노드와 자식노드들의 합을 구해야한다.
# 2. 중복 제거 방법은 괄호가 열려서 루트노드가 생성되고 자식노드가 모두 들어가고 괄호가 닫히면 딕셔너리 값 True로 설정 -> 이건 set써서 해도 될듯?
# 3. 딕셔너리 값 True이면 0 반환

import sys
input = sys.stdin.readline

visited = {}
def f(y, x, n): # y좌표, x좌표, 탐색할 정사각형 범위
    s = ""
    check = True
    temp = matrix[y][x]
    for i in range(n):
        for j in range(n):
            if temp != matrix[y+i][j+x]:    # 탐색하는 범위가 모두 같은색이 아니면 check = false
                check = False
                break

        if not check :
            break

    if check: # 탐색하는 범위가 모두 같은색이라면
        s += '1' if temp else '0'
    else:   # 모두 같은 색이 아니라면 4등분해서 재귀
        length = n // 2
        s += '('
        s += f(y, x, length)
        s += f(y, x + length, length)
        s += f(y + length, x, length)
        s += f(y + length, x + length, length)
        s += ')'

    return s    #

def dfs1(bs): # 총 루트노드와 자식노드의 합 구하는 함수
    # bs에 들어가는 문자열 형태는 (1110) 이런식으로 들어온다. 즉, 루트노드의 하위 자식노드 정보
    lv = 1
    if bs[0] == '(':
        cnt = 0
        nbs = ""
        for i in range(1, len(bs) - 1):
            if bs[i] == '(':
                cnt += 1
            elif bs[i] == ')':
                cnt -= 1
            nbs += bs[i]
            if cnt == 0:
                lv += dfs1(nbs)
                nbs = ""
    return lv

def dfs2(bs):   # 중복되는 루트노드는 합쳐주고 루트노드와 자식노드의 합 구하는 함수
    lv = 1
    if bs in visited:   # 루트노드의 정보가 visited에 들어가있다.
        return 0
    if bs[0] == '(':
        cnt = 0
        nbs = ""
        for i in range(1, len(bs) - 1):
            if bs[i] == '(':
                cnt += 1
            elif bs[i] == ')':
                cnt -= 1
            nbs += bs[i]
            if cnt == 0:
                lv += dfs2(nbs)
                if len(nbs) != 1:   # len(nbs) == 1 이면 끝까지 갔을때 체크가 안됨
                    visited[nbs] = True # 중복제거를 위해 visited 딕셔너리에 등록
                nbs = ""
    return lv

n, m = map(int, input().split())

l = 1
length = max(n, m)
while l < length:   # 문제에 가까운 2의 제곱으로 흰 칸으로 채워주기 위해 l값 설정
    l *= 2

matrix = [[False] * l for _ in range(l)]    # false 2차원 배열로 lxl 배열 생성

for i in range(n):  # input이 1일 때 matrix 값 True로 변경
    input_str = input().rstrip()
    for j in range(m):
        if input_str[j] == '1' : matrix[i][j] = True


bs = f(0, 0, l) # 재귀 들어가면서 boj 1992번처럼 루트노드와 자식노드 정보
answer1 = dfs1(bs)
answer2 = dfs2(bs)

print(answer1, answer2)
