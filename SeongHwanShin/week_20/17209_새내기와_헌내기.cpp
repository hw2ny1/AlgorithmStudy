#include<iostream>
#include<vector>
#include<algorithm>

/*
문　제　17209_새내기와_헌내기
메모리　19388 KB
시　간　176 ms

이분그래프
*/

using namespace std;

int N, ans, people[2];
bool visit[2002];
vector<int> adj[2002];

void dfs(int cur, bool old) {
	if (visit[cur]) return;
	visit[cur] = true;
	for (int i : adj[cur]) {
		if (visit[i]) continue;
		people[!old]++;
		dfs(i, !old);
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

	cin >> N;
	char a;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> a;
			if (a == '1') {
				adj[i].push_back(j);
				adj[j].push_back(i);
			}
		}
	}

	for (int i = 0; i < N; i++) {
		if (visit[i]) continue;
		people[0] = 0;
		people[1] = 0;
		dfs(i, true);
		ans += max(people[0], people[1] + 1);
	}
	cout << ans << '\n';
}