import sys
from collections import deque
input = sys.stdin.readline

L = int(input()) # 거리 ( zombie index )
gun_d, damage = map(int,input().split()) # 기관총 유효 사거리, 데미지
bomb_cnt = int(input()) # 1번 index 킬
zombie = [0]*(L+1)
q = deque() # 들어갈 값 ( 좀비 처음 index, 사거리에 들어왔을 때 진지와 좀비 거리 )
cq = deque() # 폭탄써서 죽인 좀비의 index + 사거리 -> 이 범위 안에 있는 좀비들은 기관총 덜 맞음

for i in range(1,L+1):
    zombie[i] = int(input())

for i in range(1,min(L+1,gun_d+1)) : # 사거리가 거리 길이 보다 긴 경우가 있다.
    q.append((i,i))

while q :
    s = q[0][0]
    d = q[0][1]
    if zombie[s] <= damage*(d-len(cq)) :
        # print(zombie[s],damage*(d-len(cq)))
        q.popleft()
    else :
        if bomb_cnt :
            bomb_cnt -= 1
            cq.append(s+gun_d-1)
            q.popleft()
        else :
            print("NO")
            break

    if s + gun_d <= L: q.append((s + gun_d, len(q)+1))
    if cq and s == cq[0] : cq.popleft()
else :
    print("YES")

