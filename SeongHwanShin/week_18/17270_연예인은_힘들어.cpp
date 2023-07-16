#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>

/*
문　제　17270_연예인은_힘들어
메모리　2160 KB
시　간　0 ms

지헌과 성하의 최단거리를 각각 dijkstra로 계산하고 조건에 맞는 값을 찾으면 되는 문제
문제가 묘하게 이해가 되질 않았다...
*/

using namespace std;

// 정답으로 가능한 곳이 여러개 일 경우 정보를 담을 타입
typedef struct {
	int id;
	int jd;
	int dist;
} answer;

// priority queue 비교 함수
struct compare {
	bool operator() (answer A, answer B) {
		if (A.dist != B.dist) return A.dist > B.dist;
		if (A.jd != B.jd) return A.jd > B.jd;
		if (A.id != B.id) return A.id > B.id;
	}
};

answer new_answer(int dist, int jd, int id) {
	answer ret;
	ret.id = id;
	ret.jd = jd;
	ret.dist = dist;
	return ret;
}

// 큰수
const int INF = 2111111111;

int jihun_start, sungha_start, V;
int jihun_dist[101];
int sungha_dist[101];

vector<pair<int,int>>graph[101];

// 지헌의 최단거리 계산
void dijkstra_jihun() {
	priority_queue<pair<int, int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
	int now, dist, total;

	pq.push({ 0,jihun_start });
	jihun_dist[jihun_start] = 0;

	while (!pq.empty()) {
		dist = pq.top().first;
		now = pq.top().second;
		pq.pop();

		if (jihun_dist[now] < dist) continue;

		for (auto pii : graph[now]) {
			total = dist + pii.first;
			if (jihun_dist[pii.second] > total) {
				jihun_dist[pii.second] = total;
				pq.push({ total,pii.second });
			}
		}
	}
}

// 성하의 최단거리 계산
void dijkstra_sungha() {
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	int now, dist, total;

	pq.push({ 0,sungha_start });
	sungha_dist[sungha_start] = 0;

	while (!pq.empty()) {
		dist = pq.top().first;
		now = pq.top().second;
		pq.pop();

		if (sungha_dist[now] < dist) continue;

		for (auto pii : graph[now]) {
			total = dist + pii.first;
			if (sungha_dist[pii.second] > total) {
				sungha_dist[pii.second] = total;
				pq.push({ total,pii.second });
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int M, a, b, c;
	cin >> V >> M;

	// INF로 초기화
	for (int i = 1; i <= V; i++) {
		sungha_dist[i] = INF;
		jihun_dist[i] = INF;
	}

	// 양방향 그래프
	for (int i = 0; i < M; i++) {
		cin >> a >> b >> c;
		graph[a].push_back({ c, b });
		graph[b].push_back({ c, a });
	}

	cin >> jihun_start >> sungha_start;

	dijkstra_jihun();
	dijkstra_sungha();

	priority_queue<answer,vector<answer>,compare> pq;

	int min_dist = INF;

	// 최단거리 합이 가장 작은 값을 찾음
	for (int i = 1; i <= V; i++) {
		if (i == jihun_start || i == sungha_start) continue;
		min_dist = min(min_dist, jihun_dist[i] + sungha_dist[i]);
	}

	// 조건에 맞는 경우만 pq에 넣음
	for (int i = 1; i <= V; i++) {
		if (i == jihun_start || i == sungha_start) continue;
		if (jihun_dist[i] + sungha_dist[i] != min_dist) continue;
		if (jihun_dist[i] > sungha_dist[i]) continue;
		pq.push(new_answer(jihun_dist[i] + sungha_dist[i], jihun_dist[i], i));
	}

	// 비어있을경우 후보지가 없으므로 -1
	if (pq.empty()) {
		cout << -1;
	}
	else {
		cout << pq.top().id;
	}
	return 0;
}