# 인덱스로 노드의 앞 뒤를 조회하면 시간초과 뜰 것이라고 예상 N 50만, M 150만
# 그래서 고유번호를 인덱스로해서 앞 뒤 조회할 PREV, NEXT 함수 생성 -> 조회 시간복잡도가 O(1)
# 추가하거나 제거하는 역을 기준으로 잡고 명령어가 실행될때 마다 앞 뒤 관계를 조정해준다.

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
PREV = [0]*1000001
NEXT = [0]*1000001

lst = list(map(int,input().split()))
for i in range(N) :
    k = lst[i]
    if i == 0 :
        PREV[k] = lst[-1]
        NEXT[k] = lst[1]

    elif i == N-1 :
        PREV[k] = lst[i-1]
        NEXT[k] = lst[0]

    else :
        PREV[k] = lst[i-1]
        NEXT[k] = lst[i+1]

for _ in range(M):
    command = list(input().rstrip().split())
    com = command[0]
    if com == 'BN' or com == 'BP' :
        i,j = int(command[1]), int(command[2])

        if com == 'BN' :
            a = NEXT[i]
            print(a)
            PREV[a] = j
            NEXT[j],PREV[j] = a,i
            NEXT[i] = j

        elif com == 'BP' :
            a = PREV[i]
            print(a)
            NEXT[a] = j
            PREV[j],NEXT[j] = a,i
            PREV[i] = j

    else :
        i = int(command[1])
        if com == 'CN' :
            a = NEXT[i]
            print(a)
            NEXT[i] = NEXT[a]
            PREV[NEXT[a]] = i
            PREV[a] = NEXT[a] = 0

        elif com == 'CP' :
            a = PREV[i]
            print(a)
            PREV[i] = PREV[a]
            NEXT[PREV[a]] = i
            NEXT[a] = PREV[a] = 0