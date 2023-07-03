#include<iostream>
#include<algorithm>
#include<vector>
#include<deque>

#define endl '\n'
#define MAX 258

using namespace std;

/*
문　제　1625_조명기구
메모리　2804 KB
시　간　52 ms

이 문제에서 초기 상태에서 최종 상태로 만들기 위한 쿼리는 2가지가 있다.
1. 행의 상태를 반전한다.
2. i와 j의 열을 교환한다.
둘중 먼저 알아낼 수 있는 방법은 바로 행의 상태를 반전시키는 쿼리이다.
하지만 여기서는 가정이 필요하다고 생각했다.
1부터 N번째 열까지 반복하면서 첫번째 열에 n번째 열이 정답이라고 가정하고 먼저 교환한다.
그러면 최종상태와 비교하여 행반전을 해야하는 지에 대한 답을 얻을 수 있다.
이후 열교환을 해보고 정답이 아닐경우 n+1번째 열이 정답이라고 가정하고 문제를 풀어본다.
마지막까지 정답이 나오지 않으면 -1을 출력한다.
이렇게 문제를 해결할 경우 O(MN^2)의 시간복잡도가 걸린다.
*/

using namespace std;

int N, M;
// 초기상태를 보존해 둔다.
int backup[MAX][MAX];
// 초기상태
int light[MAX][MAX];
// 최종상태
int ans[MAX][MAX];
// 열교환시 정답과 일치할경우 표시하여 재방문을 막는다.
int visited[MAX] = { 0, };

// 쿼리
struct q {
	int type;
	int a;
	int b;
};

// 새로운 쿼리 반환
q newq(int type, int a = 0, int b = 0) {
	q ret;
	ret.type = type;
	ret.a = a;
	ret.b = b;
	return ret;
}

// 쿼리를 저장해둘 동적 배열
vector<int>historyzero;
vector<pair<int, int>> historyone;

// 초기상태를 가져오고, 방문 배열을 초기화한다.
void init() {
	for (int i = 0; i < M; i++) {
		visited[i] = 0;
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			light[i][j] = backup[i][j];
		}
	}

	historyzero.clear();
	historyone.clear();
}

// 행 반전 로직
void rrever(int i) {
	int temp;
	// 첫번째 열 같은경우는 교환이 필요 없으므로 넘어간다.
	if (i) {
		// 첫번째 열과 i번째 열을 교환한다.
		for (int j = 0; j < N; j++) {
			temp = light[j][0];
			light[j][0] = light[j][i];
			light[j][i] = temp;
		}
		historyone.push_back({ 1, i + 1 });
		visited[0] += 1;
	}

	// 첫번째 열과 정답과 비교하여 항반전이 필요할 경우 반전 시킨다.
	for (int j = 0; j < N; j++) {
		if (light[j][0] != ans[j][0]) {
			for (int k = 0; k < M; k++) {
				light[j][k] = light[j][k] ? 0 : 1;
			}
			historyzero.push_back(j + 1);
		}
	}
}

// 비교하고 일치하면 true
bool compare(int cur, int cur2) {
	// 열을 비교해보고 일치하지 않으면 false
	for (int j = 0; j < N; j++) {
		if (ans[j][cur] != light[j][cur2]) return false;
	}

	// cur열과 cur2열이 일치하는데 서로 다른열 일 경우 열 교환을 수행하고 쿼리 저장
	if (cur != cur2) {
		int temp;
		for (int i = 0; i < N; i++) {
			temp = light[i][cur];
			light[i][cur] = light[i][cur2];
			light[i][cur2] = temp;
		}
		historyone.push_back({ cur + 1, cur2 + 1 });
	}

	return true;
}

// 열교환 쿼리 찾아내기
void csort() {
	deque<int> dq;
	for (int i = 0; i < M; i++) dq.push_back(i);

	// dfs 식으로 진행한다. 첫번째 열부터 정답인 열을 찾아가고 cur열에서 n번째 열과 교환할경우 n번째 열의 정답을 찾아간다.
	// 만약 cur열을 조사하고 cur+1열을 조사할경우 계단식 문제에서 쓸때없는 열교환이 많이 일어나기 때문
	int cur;
	while (!dq.empty()) {
		cur = dq.front();
		dq.pop_front();

		if (visited[cur]) continue;

		for (int i = 0; i < M; i++) {
			if (visited[i]) continue;
			if (compare(cur, i)) {
				visited[cur] += 1;
				dq.push_front(i);
				break;
			}
		}

		if (!visited[cur]) return;
	}
}

// 마지막으로 정답인지 한번더 체크한다.
int check() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (light[i][j] != ans[i][j]) {
				return 0;
			}
		}
	}
	return 1;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> M;

	int flag = 0;

	// 초기 전구 색
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> backup[i][j];
		}
	}

	// 최종 전구 색
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> ans[i][j];
		}
	}

	// 모든 열에 대해서 가정한다.
	for (int i = 0; i < M; i++) {
		init();
		rrever(i);
		csort();
		flag = check();
		if (flag) {
			// 정답일 경우 결과 출력
			cout << historyzero.size() + historyone.size() << endl;

			// i행에서 i열과 j열을 교환한 쿼리를 출력하라고 하는데,,,, 사실 이렇게 안해도 정답은 되는 것 같다.(?)
			int j = 0;
			for (auto temp : historyzero) {
				while (j < historyone.size() && historyone[j].first < temp) {
					cout << 1 << " " << historyone[j].first << " " << historyone[j].second << endl;
					j++;
				}
				cout << 0 << " " << temp << endl;
			}

			while (j < historyone.size()) {
				cout << 1 << " " << historyone[j].first << " " << historyone[j].second << endl;
				j++;
			}

			return 0;
		}
	}

	// 정답이 아닐경우
	cout << -1;
	return 0;
}