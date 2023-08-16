'''
1. 도시(cities) 이름들을 index화
2. 내일로 티켓이 있을 때(min_cost_ticket)와 없을 때(min_cost)의 교통비를 배열에 기록
3. travel_cities에 나열된 도시 순서대로 교통비 탐색
4. 내일로 티켓이 있을 때의 가격이 더 적으면 'Yes', 아니라면 'No'
'''

import sys
input = sys.stdin.readline

N, R = map(int, input().split())  # 도시 수 N, 인당 티켓 가격 R
cities = list(map(str, input().split()))
M = int(input())  # 여행 도시 수
travel_cities = list(map(str,input().split()))

# 여행 도시들을 cities의 index 번호로 바꾸기
for i in range(M):
    travel_cities[i] = cities.index(travel_cities[i])

K = int(input())  # 교통 수단 수

min_cost = [[1e9 for _ in range(N)] for _ in range(N)]
min_cost_ticket = [[1e9 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    tp, start, end, cost = map(str, input().split())
    start, end = cities.index(start), cities.index(end)
    cost = int(cost)

    min_cost[start][end] = min(cost, min_cost[start][end])
    min_cost[end][start] = min(cost, min_cost[end][start])

    if tp == 'Mugunghwa' or tp == 'ITX-Saemaeul' or tp == 'ITX-Cheongchun':
        cost = 0
    elif tp == 'S-Train' or tp == 'V-Train':
        cost /= 2
    min_cost_ticket[start][end] = min(cost, min_cost_ticket[start][end])
    min_cost_ticket[end][start] = min(cost, min_cost_ticket[end][start])

for k in range(N):
    for i in range(N):
        for j in range(N):
            min_cost[i][j] = min(min_cost[i][j], min_cost[i][k] + min_cost[k][j])
            min_cost_ticket[i][j] = min(min_cost_ticket[i][j], min_cost_ticket[i][k] + min_cost_ticket[k][j])

no_ticket_cost = yes_ticket_cost = 0
for i in range(M - 1):
    s, e = travel_cities[i], travel_cities[i + 1]

    no_ticket_cost += min_cost[s][e]
    yes_ticket_cost += min_cost_ticket[s][e]

if no_ticket_cost > yes_ticket_cost + R:
    print("Yes")
else:
    print("No")