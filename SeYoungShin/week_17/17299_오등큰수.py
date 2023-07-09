'''
이와 비슷한 문제를 이전에 풀었어서 스택으로 접근함
1. 횟수를 F 리스트로 카운트
2. 본인보다 등장한 횟수가 큰 원소가 나올때까지 pop
3. 스택이 비어있다면 오등큰수가 없으므로 -1 / 있다면 원래의 수 저장
'''

import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
F = [0] * (max(A) + 1)
for a in A:
    F[a] += 1

stack = []
ans = [0] * N
for i in range(-1, -N - 1, -1):
    while stack and stack[-1][0] <= F[A[i]]:
        stack.pop()
    if not stack:
        ans[i] = -1
    else:
        ans[i] = stack[-1][1]
    stack.append((F[A[i]], A[i]))
print(*ans)