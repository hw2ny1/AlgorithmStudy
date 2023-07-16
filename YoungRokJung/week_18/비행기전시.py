import sys
from collections import deque
input = sys.stdin.readline

N,M,T = map(int,input().split())

zero = deque()
one = deque()

for num in range(N):
    d,m,r = map(int,input().split())
    if d == 0 :
        zero.append([num,m,r])
    else :
        one.append([num,m,r])

cd = 0  # 현재 위치
ct = 0  # 현재 시간
ans = [[] for _ in range(N)]
while (zero or one) :

    w = 0 # 현재 적재량
    if cd == 0 : # 현재 위치가 0일 때
        if zero : # 0번 위치에 남은 부품이 있을 때
            if one and ct < zero[0][2] and one[0][2] < zero[0][2] :
                # 1번 위치에 부품이 있고, 0번 위치의 가장 앞 준비시간이 현재시간보다 크고,
                # 1번 위치의 가장 앞 부품의 준비시간이 0번 위치의 가장 앞 준비시간보다 작을 때
                if ct < one[0][2] :
                # 현재 시간이 1번 위치의 가장 앞 부품의 준비시간보다 작다면 1번 위치의 준비시간을 기다리고 T를 더해준다
                    ct = one[0][2] + T
                    cd = 1

                else :
                # 아니라면 1번 위치로 이동하는 시간만 더해준다.
                    ct += T
                    cd = 1

                continue

            if zero[0][2] > ct :
            # 0번 위치 부품의 준비시간이 현재 시간보다 크다면 준비시간까지 기다린다.
                ct = zero[0][2]
                continue

            while zero and zero[0][2] <= ct and w < M:
            # 현재시간보다 준비시간이 작은것들, 무게 적재량이 M보다 작을 때까지
                number,a,b = zero.popleft()
                if w + a <= M :
                # 한번에 담을 수 있다면 시작,끝 시간을 바로 저장
                    w += a
                    ans[number].append(ct)
                    ans[number].append(ct+T)
                else :
                # 한번에 못담고 분해해야된다면 시작시간만 저장
                    zero.appendleft([number,w+a-M,b])
                    ans[number].append(ct)
                    break

            # 1번으로 이동
            ct += T
            cd = 1

        else : # 0 번에 남은 부품이 없을 때는 다시 1번으로 돌아감
            ct += T
            cd = 1

    else :  # 0번과 완전 반대 ( 설명 생략 )
        if one :
            if zero and ct < one[0][2] and zero[0][2] < one[0][2] :
                if ct < zero[0][2]:
                    ct = zero[0][2] + T
                    cd = 0

                else:
                    ct += T
                    cd = 0
                continue

            if one[0][2] > ct :
                ct = one[0][2]
                continue

            while one and one[0][2] <= ct and w < M :
                number,a,b = one.popleft()
                if w + a <= M :
                    w += a
                    ans[number].append(ct)
                    ans[number].append(ct + T)

                else :
                    one.appendleft([number,w+a-M,b])
                    ans[number].append(ct)
                    break

            cd = 0
            ct += T
        else :
            ct += T
            cd = 0

# ans에는 시작과, 끝 시간이 저장
for lst in ans :
    print(lst[0],lst[-1])