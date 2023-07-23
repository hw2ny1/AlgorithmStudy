import sys
input = sys.stdin.readline

"""
문　제　12929_빌딩_높이
메모리　31256 KB
시　간　56 ms

어떻게 풀지 생각은 했는데 구현이 어려워 참고(?)를 했습니다.
"""

N, K = map(int,input().split())
M = int(input())
X = [1] + list(map(int,input().split()))
T = [0] + list(map(int,input().split()))

ans = 0
M += 1

if M < 2:
    print(K*(N-1))
    exit(0)

for i in range(1, M):
    T[i] = min(T[i], T[i - 1] + K * (X[i] - X[i - 1]))

for i in range(M-2,-1,-1):
    T[i] = min(T[i], T[i + 1] - K * (X[i] - X[i + 1]))

for i in range(M-1):
    if T[i] >= T[i + 1] + K * (X[i + 1] - X[i]):
        ans = max(ans, T[i+1] + K * (X[i + 1] - X[i]))

    elif T[i+1] >= T[i] + K * (X[i+1] - X[i]):
        ans = max(ans, T[i] + K * (X[i+1] - X[i]))

    else:
        x = X[i]
        d = X[i+1] - X[i]
        while d:
            while x + d <= X[i + 1] and T[i] + K * (x + d - X[i]) <= T[i + 1] - K * (x + d - X[i + 1]):
                x += d
            d >>= 1
        ans = max(ans, T[i] + K * (x - X[i]))
        if x < X[i + 1]:
            ans = max(ans, T[i+1] - K * (x+1 - X[i+1]))

print(max(ans, T[M-1] + K*(N - X[M-1])))