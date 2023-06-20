#include<iostream>
#include<algorithm>
#include<vector>

/*
문　제　16235_나무_재테크
메모리　236400 KB
시　간　232 ms

처음엔 쉬울 줄 알았는데 반복문으로 계속 탐색하면서 할 경우 시간초과가 뜸

따라서 나무위치와 나이를 저장할 리스트를 구현했는데 시간초과가 뜸

그래서 리스트 나이별로 만들어 나무좌표만 저장하고 시간을 최대한 아끼기 위해 연결리스트 노드를 1000만개 만듬

나무 나이가 110을 넘기기 힘들다고 생각했는데 넘기는 테스트케이스가 있는 것 같아서 MaxAge를 140까지 늘림

정답은 맞았지만 메모리도 시간도 좋은 방법은 아닌 것같다. 오기가 생겨서 풀긴 했는데 나이별로 저장할 생각을 했는데 그냥 좌표별로 카운트할 생각을 왜 못했을까

그래도 STL쓰지않고 연결리스트 구현한 해본 것은 좋은 경험이 된것 같다.
*/

#define MaxAge 140

using namespace std;

// 연결 리스트 구현

struct tree {
    int x;
    int y;
    tree* next;
    tree* prev;
    tree() :x(0), y(0), next(nullptr), prev(nullptr) { }
}tr[10000000];

int cnt;

tree* getNewTree(int x = 0, int y = 0, tree* pv = nullptr) {
    tree* ret = &tr[cnt++];
    ret->x = x;
    ret->y = y;
    ret->prev = pv;
    ret->next = nullptr;
    return ret;
}

struct tree_list {
    tree* head;
    tree* tail;
    int size;

    void clear() {
        head = getNewTree();
        tail = head;
        size = 0;
    }

    void push(tree* temp) {
        tail->next = temp;
        temp->prev = tail;
        tail = temp;
        size++;
    }
};

int N, M, K;
int delta[8][2] = { {-1,-1}, {-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1} };

int nourishment[11][11] = { 0, };   // 겨울에 추가되는 양분 양
int food[11][11];                   // 땅에 남아있는 양분 양
int temp[11][11] = { 0, };          // 죽은 나무 양분 양
tree_list List[MaxAge + 1];           // 나이마다 나무를 저장

void spring() {
    for (int i = 1; i <= MaxAge; i++) {
        if (List[i].head->next == nullptr) continue;

        auto iter = List[i].head->next;
        while (iter != nullptr) {
            if (food[iter->x][iter->y] < i) {
                temp[iter->x][iter->y] += (i / 2);
                List[i].size--;

                if (iter->next == nullptr) {
                    iter->prev->next = nullptr;
                }
                else {
                    iter->next->prev = iter->prev;
                    iter->prev->next = iter->next;
                }

                iter = iter->next;
            }
            else {
                food[iter->x][iter->y] -= i;
                iter = iter->next;
            }
        }
    }

    for (int i = MaxAge; i >= 0; i--) {
        List[i + 1].head = List[i].head;
        List[i + 1].tail = List[i].tail;
        List[i + 1].size = List[i].size;
    }
    List[0].clear();
}

void summer() {
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            food[i][j] += temp[i][j];
            temp[i][j] = 0;
        }
    }
}

void fall() {
    int nx, ny;
    for (int i = 5; i <= MaxAge; i += 5) {
        if (List[i].head->next == nullptr) continue;
        auto iter = List[i].head->next;
        while (iter != nullptr) {
            for (int k = 0; k < 8; k++) {
                nx = iter->x + delta[k][0];
                ny = iter->y + delta[k][1];
                if (nx < 1 || nx > N || ny < 1 || ny > N) continue;
                List[1].push(getNewTree(nx, ny, List[1].tail));
            }

            iter = iter->next;
        }
    }
}

void winter() {
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            food[i][j] += nourishment[i][j];
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int x, y, z;

    cin >> N >> M >> K;

    cnt = 0;

    for (int i = 0; i <= MaxAge; i++) {
        List[i].head = getNewTree();
        List[i].tail = List[i].head;
    }

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            cin >> nourishment[i][j];
            food[i][j] = 5;
        }
    }

    for (int i = 0; i < M; i++) {
        cin >> x >> y >> z;
        List[z].push(getNewTree(x, y, List[z].tail));
    }

    for (int i = 1; i <= K; i++) {
        spring();
        summer();
        fall();
        winter();
    }

    int ans = 0;
    for (int i = 0; i < 110; i++) {
        ans += List[i].size;
    }
    cout << ans;
    return 0;
}
