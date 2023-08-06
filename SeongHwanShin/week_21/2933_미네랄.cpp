#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>

/*
문　제　2933_미네랄
메모리　2308 KB
시　간　24 ms

참고해서 풀었습니다
*/

using namespace std;

char board[100][100];
int dy[4] = { -1,0,1,0 };
int dx[4] = { 0,1,0,-1 };
int n, m;
vector<int> v;

void input() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> board[i][j];
        }
    }
    int t;
    cin >> t;
    v.resize(t);
    for (int i = 0; i < t; i++)
        cin >> v[i];
}


bool is_range(int y, int x) {
    return 0 <= y && y < n && 0 <= x && x < m;
}

pair<int, int> Throw(int h, int cnt) {
    int y = n - h;
    int x = cnt % 2 == 0 ? 0 : m - 1;
    while (is_range(y, x) && board[y][x] == '.') {
        x += cnt % 2 == 0 ? 1 : -1;
    }
    return { y,x };
}

bool cmp(pair<int, int> a, pair<int, int> b) {
    return a.first > b.first;
}

void bfs(pair<int, int> p) {
    int check[100][100] = { 0 };
    queue<pair<int, int>> q;
    for (int i = 0; i < m; i++) {
        if (board[n - 1][i] == 'x') {
            q.push({ n - 1,i });
            check[n - 1][i] = 1;
        }
    }
    //바닥에있는 클러스터 연결
    while (!q.empty()) {
        int y, x;
        y = q.front().first;
        x = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (is_range(ny, nx) && check[ny][nx] == 0 && board[ny][nx] == 'x') {
                q.push({ ny,nx });
                check[ny][nx] = 1;
            }
        }
    }

    //공중에있는 클러스터
    vector<pair<int, int>> dv;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] == 'x' && check[i][j] == 0) {
                dv.push_back({ i,j });
            }
        }
    }
    sort(dv.begin(), dv.end(), cmp);

    vector<pair<int, int>> dv2 = dv;
    while (!dv.empty()) {
        vector<pair<int, int>> temp;
        bool flag = false;
        for (int i = 0; i < dv.size(); i++) {
            int y = dv[i].first + 1;
            int x = dv[i].second;
            if (!is_range(y, x)) { flag = true; break; }
            if (check[y][x]) { flag = true; break; }
            temp.push_back({ y,x });
        }
        if (flag)break;
        dv = temp;
    }
    for (auto t : dv2)
        board[t.first][t.second] = '.';
    for (auto t : dv)
        board[t.first][t.second] = 'x';
}
void print() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << board[i][j];
        }
        cout << "\n";
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    input();
    for (int i = 0; i < v.size(); i++) {
        pair<int, int> p = Throw(v[i], i);
        if (!is_range(p.first, p.second))continue;
        board[p.first][p.second] = '.';
        bfs(p);
    }
    print();
}