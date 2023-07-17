'''
시작점 두개를 기준으로 각각 거리 측정한 후
조건 1, 2, 3, 4에 맞는 최종 약속 장소 선정
'''

def dijkstra(start, visit):
    q = []
    heapq.heappush(q, (0, start))
    visit[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if visit[now] < dist:
            continue
        for ndist, next in connect[now]:
            nextdist = visit[now] + ndist
            if visit[next] > nextdist:
                visit[next] = nextdist
                heapq.heappush(q, (nextdist, next))

import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize
V, M = map(int, input().split())

# 지헌, 성하 기준 다익스트라
connect = [[] for _ in range(V + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    connect[a].append((c, b))
    connect[b].append((c, a))
J, S = map(int, input().split())
visitJ = [inf for _ in range(V + 1)]
visitS = [inf for _ in range(V + 1)]
dijkstra(J, visitJ)
dijkstra(S, visitS)

# 최종 약속 장소 선정
mintime = distJ = inf
ans = -1
for v in range(1 ,V + 1):
    if v != J and v != S:
        mintime = min(mintime, visitJ[v] + visitS[v])
for v in range(1, V + 1):
    if v != J and v != S:
        if visitJ[v] + visitS[v] == mintime and visitJ[v] <= visitS[v]:
            if visitJ[v] < distJ:
                ans = v
                distJ = visitJ[v]
print(ans)