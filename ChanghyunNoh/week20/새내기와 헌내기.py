import sys
input = sys.stdin.readline

N = int(input())
adj = []
for i in range(N):
    adj.append(list(map(int, input().split())))
answer = 0
def dfs(isTrue, who):
    global cnt
    global answer
    if isTrue:
        lier = 1
    else:
        cnt += 1
        if cnt > answer:
            answer = cnt
        lier = 0
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            if adj[i] == lier:
                dfs(False, i)
            else:
                dfs(True, i)

cnt = 0
visited = [False] * N
visited[0] = True
dfs(True, 0)

cnt = 0
visited = [False] * N
visited[0] = True
dfs(False, 0)

print(answer)