import sys
input = sys.stdin.readline
import heapq
inf = 1e10

V, M = map(int, input().split())
adj = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    adj[a][b] = min(adj[a][b], c)
    adj[b][a] = min(adj[b][a], c)

J, S = map(int, input().split())
jh = [inf] * (V + 1)
sh = [inf] * (V + 1)

def djikstra(x, visited):
    visited[x] = 0
    pq = []
    for i in range(1, V + 1):
        if adj[x][i]:
            heapq.heappush(pq, (adj[x][i], i))
            visited[i] = adj[x][i]
    while pq:
        tmp = heapq.heappop(pq)
        d = tmp[0]
        now = tmp[1]
        if visited[now] < d:
            continue
        for nxt in range(1, V + 1):
            if not adj[now][nxt]:
                continue
            if visited[now] + adj[now][nxt] < visited[nxt]:
                visited[nxt] = visited[now] + adj[now][nxt]
                heapq.heappush(pq, (visited[nxt], nxt))
    return visited
jh = djikstra(J, jh)
sh = djikstra(S, sh)

dist = inf
ans = -1
j = inf
for i in range(1, V + 1):
    if i == J or i == S:
        continue
    if jh[i] + sh[i] <= dist and jh[i] <= sh[i]:
        if jh[i] < j:
            j = jh[i]
            dist = jh[i] + sh[i]
            ans = i

print(ans)