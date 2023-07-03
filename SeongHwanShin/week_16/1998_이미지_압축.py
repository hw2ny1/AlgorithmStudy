import sys
import bisect
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

"""
문　제　1998_이미지_압축
메모리　36308 KB
시　간　80 ms

쿼드트리를 생성한다. 정점의 수의 경우 재귀가 들어가는 횟수와 일치한다.

압축의 경우 dict을 만들면 쉽다고 생각했다. 그러나 BWWB 같은 경우뿐만 아니라 더 큰 이미지의 경우도 압축할 수 있다고 한다.

이 경우 어떻게 확인해야할까 정말 많이 고민했는데, 사실 중복이면 그냥 값을 더하지 않으면 상위 노드에서 중복을 확인하더라도 마찬가지로 값을 더하지 않으면 된다는 사실을 알았다.
"""


def slice(x, y, n, m):
    global ans1
    ans1 += 1
    c = graph[x][y]
    if n == 1:
        return ['W',1] if c == '1' else ['B',1]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != c:
                c1, n1 = slice(x, y, n // 2,4*m-2)
                c2, n2 = slice(x, y + n // 2, n // 2,4*m-1)
                c3, n3 = slice(x + n // 2, y, n // 2,4*m)
                c4, n4 = slice(x + n // 2, y + n // 2, n // 2,4*m+1)

                temp = 'R' + c1 + c2 + c3 + c4
                num = 1 + n1 + n2 + n3 + n4

                if not save[temp]:
                    save[temp] = num
                if temp in visited:
                    return [temp, 0]
                else:
                    visited.add(temp)
                return [temp, num]

    return ['W',1] if c == '1' else ['B',1]


def get(N, M):
    arr = []
    for i in range(8):arr.append(pow(2,i))
    N = bisect.bisect_left(arr,N)
    M = bisect.bisect_left(arr,M)
    return max(arr[N],arr[M])


N, M = map(int,input().split())
K = get(N,M)
graph = [['0' for _ in range(K)] for _ in range(K)]

for i in range(N):
    temp = input().rstrip()
    for j in range(M):
        graph[i][j] = temp[j]

visited = set()

save = defaultdict(int)

ans1 = 0
result, num = slice(0,0,K,1)

print(ans1, num)