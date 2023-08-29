import sys
input = sys.stdin.readline
from collections import deque

L = int(input())  # 거리
distance, damage = map(int, input().split())  # 사거리, 데미지
ammo = int(input())  # 수평 세열 지향성 지뢰 개수
zombie = []

queue = deque()
ammo_cnt = 0
ans = True

for i in range(L):
    z = int(input())
    zombie.append(z)

# 기관총 사정범위 내
for i in range(min(L, distance)):
    if not ammo_cnt:  # 지뢰를 아직 사용 안했을 경우
        if zombie[i] - damage * (i + 1) <= 0:
            queue.append(0)
        else:
            queue.append(zombie[i] - damage * (i + 1))
            ammo_cnt += 1
    else:
        if zombie[i] - damage * (i + 1 - ammo_cnt) <= 0:
            queue.append(0)
        else:
            queue.append(zombie[i] - damage * (i + 1 - ammo_cnt))
            ammo_cnt += 1

# 기관총 사정범위 바깥
for i in range(distance, L):
    if queue[0] == 0:
        queue.popleft()
        if zombie[i] - damage * (distance - ammo_cnt) <= 0:
            queue.append(0)
        else:
            queue.append(zombie[i] - damage * (distance - ammo_cnt))
            ammo_cnt += 1
    else:
        queue.popleft()
        if ammo:
            ammo -= 1
        else:
            ans = False
            break

        if zombie[i] - damage * (distance - ammo_cnt) <= 0:
            queue.append(0)
            ammo_cnt -= 1
        else:
            queue.append(zombie[i] - damage * (distance - ammo_cnt))

while queue:
    if queue[0] == 0:
        queue.popleft()
    else:
        queue.popleft()
        ammo_cnt -= 1
        if ammo:
            ammo -= 1
        else:
            ans = False
            break

if ans:
    print("YES")
else:
    print("NO")