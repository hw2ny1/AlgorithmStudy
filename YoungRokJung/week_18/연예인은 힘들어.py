# 지헌이의 위치, 성하의 위치에서 각 노드별 최소거리를 구해준다 ( 다익스트라 )
# 지헌이와의 거리 + 성하와의 거리의 최소 값이고 지헌이와의 거리, 번호 순서가 작은 것 순으로 정렬
# 이런 노드가 있다면 제일 앞에 오는 노드가 정답, 아니면 -1 출력

import sys,heapq
input = sys.stdin.readline

V,M = map(int,input().split())
graph = [[] for _ in range(V+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

J,S = map(int,input().split())

INF = sys.maxsize
distance_j = [INF] * (V+1)
distance_s = [INF] * (V+1)

# 기본 다익스트라
def dijkstra(v,distance) :
    q = []
    distance[v] = 0
    heapq.heappush(q,(0,v))

    while q :
        dist,node = heapq.heappop(q)

        if distance[node] > dist : continue

        for v,d in graph[node] :
            if distance[v] > distance[node] + d :
                distance[v] = distance[node] + d
                heapq.heappush(q,(distance[v],v))

    return distance


a = dijkstra(J,distance_j) # 지헌이의 거리정보
b = dijkstra(S,distance_s) # 성하의 거리정보
ans_list = []
MIN = sys.maxsize

#거리, 지헌이와의 거리, 번호 순서
for i in range(1,V+1) :
    if i == J or i == S : continue # 지헌이와 성하의 위치는 패스
    MIN = min(a[i]+b[i],MIN)       # 거리 합 최소 값 갱신
    ans_list.append((a[i]+b[i],a[i],i)) # 거리, 지헌이와의 거리, 위치 번호 순으로 저장

ans_list.sort() # 정렬
ans = sys.maxsize
for i in range(len(ans_list)) :
    if ans_list[i][0] == MIN and ( a[ans_list[i][2]] <= b[ans_list[i][2]]) :
        # 거리 값이 최소 값이고, 그 위치의 지헌이와의 거리가 성하와의 거리보다 작거나 같으면 답
        print(ans_list[i][2])
        break
else :
    print(-1)