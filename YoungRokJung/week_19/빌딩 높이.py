def main():
    N, K = map(int, input().split())

    M = int(input())

    X = []
    T = []

    # 만약 M이 0보다 크다면 X와 T를 입력
    if M:
        X = list(map(int, input().split()))
        T = list(map(int, input().split()))

    # 만약 X가 비어있지 않고, X의 첫 번째 원소가 1이라면 T의 첫 번째 원소를 0으로 설정
    if X and X[0] == 1:
        T[0] = 0
    else:
    # X와 T의 맨 앞에 1과 0을 추가하여 M의 크기를 1 증가
        X.insert(0, 1)
        T.insert(0, 0)
        M += 1

    # 만약 M이 2보다 작다면, 즉 X와 T의 크기가 1 이하라면 (K * (N - 1))을 출력하고 프로그램을 종료
    if M < 2:
        print(K * (N - 1))
        return

    # X와 T를 순방향으로 탐색하며 각 원소를 자신과 바로 앞 원소의 값에 따라 수정
    for i in range(1, M):
        T[i] = min(T[i], T[i - 1] + K * (X[i] - X[i - 1]))

    # X와 T를 역방향으로 탐색하며 각 원소를 자신과 바로 뒤 원소의 값에 따라 수정
    for i in range(M - 2, 0, -1):
        T[i] = min(T[i], T[i + 1] - K * (X[i] - X[i + 1]))

    # 최대 값을 저장할 변수 ans를 0으로 초기화
    ans = 0

    # X와 T를 순차적으로 탐색하면서 최대 값 탐색
    for i in range(M - 1):
        # T[i]가 T[i + 1] + K * (X[i + 1] - X[i]) 보다 크거나 같으면,
        # i번째 빌딩의 높이를 X[i + 1]의 높이로 설정
        if T[i] >= T[i + 1] + K * (X[i + 1] - X[i]):
            ans = max(ans, T[i + 1] + K * (X[i + 1] - X[i]))
        # T[i + 1]이 T[i] + K * (X[i + 1] - X[i]) 보다 크거나 같으면,
        # (i+1)번째 빌딩의 높이를 X[i]의 높이로 설정
        elif T[i + 1] >= T[i] + K * (X[i + 1] - X[i]):
            ans = max(ans, T[i] + K * (X[i + 1] - X[i]))
        else:
            # 그 외의 경우, 이진 탐색을 통해 적절한 높이 탐색
            x = X[i]
            d = X[i + 1] - X[i]
            while d:
                while x + d <= X[i + 1] and T[i] + K * (x + d - X[i]) <= T[i + 1] - K * (x + d - X[i + 1]):
                    x += d
                d >>= 1
            # 이진 탐색을 통해 찾은 높이로 높이 제한을 만족하도록 합니다.
            ans = max(ans, T[i] + K * (x - X[i]))
            if x < X[i + 1]:
                ans = max(ans, T[i + 1] - K * (x + 1 - X[i + 1]))

    # 마지막 원소를 처리
    ans = max(ans, T[M - 1] + K * (N - X[M - 1]))

    print(ans)


# main 함수를 호출하여 프로그램을 실행합니다.
main()
