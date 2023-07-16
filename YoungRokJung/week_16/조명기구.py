from collections import deque

N, M = map(int, input().split())

MAX = 258

# 초기상태를 보존해 둔다.
backup = [[0] * MAX for _ in range(MAX)]
# 초기상태
light = [[0] * MAX for _ in range(MAX)]
# 최종상태
ans = [[0] * MAX for _ in range(MAX)]
# 열교환시 정답과 일치할경우 표시하여 재방문을 막는다.
visited = [0] * MAX

# 쿼리
class Query:
    def __init__(self, type, a=0, b=0):
        self.type = type
        self.a = a
        self.b = b

# 쿼리를 저장해둘 동적 배열
historyzero = []
historyone = []

# 초기상태를 가져오고, 방문 배열을 초기화한다.
def init():
    for i in range(M):
        visited[i] = 0

    for i in range(N):
        for j in range(M):
            light[i][j] = backup[i][j]

    historyzero.clear()
    historyone.clear()

# 행 반전 로직
def rrever(i):
    # 첫번째 열 같은경우는 교환이 필요 없으므로 넘어간다.
    if i:
        # 첫번째 열과 i번째 열을 교환한다.
        for j in range(N):
            light[j][0], light[j][i] = light[j][i], light[j][0]
        historyone.append((1, i + 1))
        visited[0] += 1

    # 첫번째 열과 정답과 비교하여 항반전이 필요할 경우 반전 시킨다.
    for j in range(N):
        if light[j][0] != ans[j][0]:
            for k in range(M):
                light[j][k] = 0 if light[j][k] else 1
            historyzero.append(j + 1)

# 비교하고 일치하면 True
def compare(cur, cur2):
    # 열을 비교해보고 일치하지 않으면 False
    for j in range(N):
        if ans[j][cur] != light[j][cur2]:
            return False

    # cur열과 cur2열이 일치하는데 서로 다른열 일 경우 열 교환을 수행하고 쿼리 저장
    if cur != cur2:
        for i in range(N):
            light[i][cur], light[i][cur2] = light[i][cur2], light[i][cur]
        historyone.append((cur + 1, cur2 + 1))

    return True

# 열교환 쿼리 찾아내기
def csort():
    dq = deque(range(M))

    # dfs 식으로 진행한다. 첫번째 열부터 정답인 열을 찾아가고 cur열에서 n번째 열과 교환할경우 n번째 열의 정답을 찾아간다.
    # 만약 cur열을 조사하고 cur+1열을 조사할경우 계단식 문제에서 쓸때없는 열교환이 많이 일어나기 때문
    while dq:
        cur = dq.popleft()

        if visited[cur]:
            continue

        for i in range(M):
            if visited[i]:
                continue
            if compare(cur, i):
                visited[cur] += 1
                dq.appendleft(i)
                break

        if not visited[cur]:
            return

# 마지막으로 정답인지 한번더 체크한다.
def check():
    for i in range(N):
        for j in range(M):
            if light[i][j] != ans[i][j]:
                return 0
    return 1

# 초기 전구 색
for i in range(N):
    backup[i] = list(map(int, input().split()))

# 최종 전구 색
for i in range(N):
    ans[i] = list(map(int, input().split()))

flag = 0

# 모든 열에 대해서 가정한다.
for i in range(M):
    init()
    rrever(i)
    csort()
    flag = check()
    if flag:
        # 정답일 경우 결과 출력
        print(len(historyzero) + len(historyone))

        # i행에서 i열과 j열을 교환한 쿼리를 출력하라고 하는데,,,, 사실 이렇게 안해도 정답은 되는 것 같다.(?)
        j = 0
        for temp in historyzero:
            while j < len(historyone) and historyone[j][0] < temp:
                print(1, historyone[j][0], historyone[j][1])
                j += 1
            print(0, temp)

        while j < len(historyone):
            print(1, historyone[j][0], historyone[j][1])
            j += 1

        exit(0)

# 정답이 아닐경우
print(-1)
