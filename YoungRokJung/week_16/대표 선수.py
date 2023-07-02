# 1. 일단 팀의 대표선수들을 모아두고 거기서 비교해야한다.
# 2. 대표선수들의 그룹에서 최대 - 최소 를 해서 ans 랑 비교해야함
# 3. 대표 그룹에서 최소 값을 가진 학생을 그 반의 그 다음 학생으로 갱신함
# 4. 갱신하는 과정에서 MAX값이 변할 수 있으니 갱신해준다. 그리고 반복하며 MAX - 대표그룹의 최소값
# 5. 근데 반의 몇번째 학생인지 알아야 하므로 index_cnt를 생성하여 현재 몇반 몇번째 학생인지 나타낸다.
# 6. 갱신하다가 index_cnt[반] 값이 학생 수 M을 넘기면 종료한다.

import sys,heapq
input = sys.stdin.readline

N,M = map(int,input().split()) # N 학급, M 각 학급의 학생 수

MAX = 0
index_cnt = [0]*N # i행 팀의 몇번째 학생인지
team = []
q = []  # 뽑힌 학생들 들어갈 queue

for i in range(N):
    lst = sorted(list(map(int,input().split())))
    MAX = max(MAX,lst[0])   # 초기 q의 MAX값 설정
    heapq.heappush(q, (lst[0],i)) # q에 (값, 반) heap으로 등록
    team.append(lst) # 학생 오름차순으로 정렬하고 팀 등록

ans = sys.maxsize
while q: # 대표 그룹
    now = heapq.heappop(q) # 대표 그룹에서 최소값을 가진 학생의 정보를 추출
    min_value = now[0]      # 대표 그룹의 최소 값
    min_idx = now[1]        # 그 학생의 반

    ans = min(MAX - min_value, ans) # 구해야하는 답은 대표그룹의 최대 - 최소

    index_cnt[min_idx] += 1 # 최소 값을 가진 학생을 빼고 그 다음 학생을 등록
    if index_cnt[min_idx] == M : # 그 다음 학생이 없다면 종료
        break

    MAX = max(MAX,team[min_idx][index_cnt[min_idx]]) # 갱신과정에서 MAX와 다음 학생과 비교하여 MAX값 갱신
    heapq.heappush(q,(team[min_idx][index_cnt[min_idx]],min_idx)) # 대표그룹에 등록

print(ans)