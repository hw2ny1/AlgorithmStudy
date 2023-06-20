#include<iostream>
#include<algorithm>
#include<vector>

/*
문　제　12869_뮤탈리스크
메모리　2908 KB
시　간　0 ms

처음엔 그리디문제 처럼 가장 높은 체력부터 때리면 된다고 생각했으나 다른 방법이 더 빠름
백트래킹으로 풀면 된다 생각 했으나 생각 보다 경우의 수가 많음
그래서 중복 계산을 방지하기 위해 dp 배열
*/

using namespace std;

// 중복 계산 방지를 위한 dp 배열
int dp[61][61][61] = { 0, };

int func(int a, int b, int c) {
    // 음수면 0
    if (a < 0) a = 0;
    if (b < 0) b = 0;
    if (c < 0) c = 0;

    if (a == 0 && b == 0 && c == 0) return 0;

    if (dp[a][b][c] != 999) return dp[a][b][c];

    dp[a][b][c] = min(dp[a][b][c], func(a - 9, b - 3, c - 1) + 1);
    dp[a][b][c] = min(dp[a][b][c], func(a - 9, b - 1, c - 3) + 1);
    dp[a][b][c] = min(dp[a][b][c], func(a - 3, b - 9, c - 1) + 1);
    dp[a][b][c] = min(dp[a][b][c], func(a - 3, b - 1, c - 9) + 1);
    dp[a][b][c] = min(dp[a][b][c], func(a - 1, b - 3, c - 9) + 1);
    dp[a][b][c] = min(dp[a][b][c], func(a - 1, b - 9, c - 3) + 1);

    return dp[a][b][c];
}



int N;
int main() {
    cin >> N;
    for (int i = 0; i < 61; i++) {
        for (int j = 0; j < 61; j++) {
            for (int k = 0; k < 61; k++) {
                dp[i][j][k] = 999;
            }
        }
    }

    vector<int> scv;
    for (int i = 0; i < N; i++) {
        int hp;
        cin >> hp;
        scv.push_back(hp);
    }
    cout << func(scv[0], scv[1], scv[2]) << '\n';


    return 0;
}