#include<iostream>
#include<algorithm>
#include<vector>
#include<deque>

/*
문　제　25604_비행기 전시
메모리　2204 KB
시　간　0 ms

상황에 따른 시뮬레이션을 구현하면 되는 문제.

문제 이해가 어려웠다.
*/

using namespace std;

int N, M, T;

vector<int> order;

typedef struct {
	int id;
	int time;
	int weight;
} parts;

parts getNew(int x, int y, int z) {
	parts ret;
	ret.id = x;
	ret.time = y;
	ret.weight = z;
	return ret;
}

deque<parts> zero_point;
deque<parts> one_point;

vector<int> zero_ans[1001];
vector<int> one_ans[1001];

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> M >> T;

	int temp, a, b;
	int cnt0 = 0;
	int cnt1 = 0;
	for (int i = 0; i < N; i++) {
		cin >> temp >> a >> b;
		// 순서 기억
		order.push_back(temp);
		// 각 포인트에 맞춰서 { id, 준비 시간, 무게 } 로 push
		if (temp) {
			one_point.push_back(getNew(cnt0++, b, a));
		}
		else {
			zero_point.push_back(getNew(cnt1++, b, a));
		}
	}

	int Time = 0;
	int flag = 0;
	while (zero_point.size() || one_point.size()) {
		int cage = 0;

		// 0번
		if (flag == 0) {
			// 준비된 화물들 다 담음
			while (zero_point.size() and Time >= zero_point.front().time and cage < M) {
				if (cage + zero_point.front().weight <= M) {
					cage += zero_point.front().weight;
					
					// 기록
					if (zero_ans[zero_point.front().id].size()) {
						zero_ans[zero_point.front().id].push_back(Time + T);
					}
					else {
						zero_ans[zero_point.front().id].push_back(Time);
						zero_ans[zero_point.front().id].push_back(Time + T);
					}
					zero_point.pop_front();
				}
				// 만약 초과할 경우 분해해서 담음
				else {
					auto temp = zero_point.front();
					zero_ans[zero_point.front().id].push_back(Time);

					int less = M - cage;
					cage = M;
					temp.weight -= less;
					zero_point.pop_front();
					zero_point.push_front(temp);
				}
			}

			// 화물을 담았다면?
			if (cage) {
				flag = 1;
				Time += T;
			}
			// 담지 않았다면
			else {
				// 0번이 비었다면
				if (zero_point.empty()) {
					flag = 1;
					Time += T;
				}
				// 1번이 비었다면
				else if (one_point.empty()) {
					Time = zero_point.front().time;
				}
				// 둘다 있다면 빠른쪽으로
				else {
					if (zero_point.front().time <= one_point.front().time) {
						Time = zero_point.front().time;
					}
					else {
						flag = 1;
						// 기다렸다 가거나 바로가거나
						if (one_point.front().time < Time) {
							Time += T;
						}
						else {
							Time = one_point.front().time + T;
						}
					}
				}
			}
		}
		// 1번
		else {
			// 준비된 화물들 다 담음
			while (one_point.size() and Time >= one_point.front().time and cage < M) {
				if (cage + one_point.front().weight <= M) {
					cage += one_point.front().weight;

					// 기록
					if (one_ans[one_point.front().id].size()) {
						one_ans[one_point.front().id].push_back(Time + T);
					}
					else {
						one_ans[one_point.front().id].push_back(Time);
						one_ans[one_point.front().id].push_back(Time + T);
					}

					one_point.pop_front();
				}
				// 만약 초과할 경우 분해해서 담음
				else {
					auto temp = one_point.front();
					one_ans[one_point.front().id].push_back(Time);

					int less = M - cage;
					cage = M;
					temp.weight -= less;
					one_point.pop_front();
					one_point.push_front(temp);
				}
			}

			// 화물을 담았다면?
			if (cage) {
				flag = 0;
				Time += T;
			}
			// 담지 않았다면
			else {
				// 1번이 비었다면
				if (one_point.empty()) {
					flag = 0;
					Time += T;
				}
				// 0번이 비었다면
				else if (zero_point.empty()) {
					Time = one_point.front().time;
				}
				// 둘다 있다면 빠른쪽으로
				else {
					if (one_point.front().time <= zero_point.front().time) {
						Time = one_point.front().time;
					}
					else {
						flag = 0;
						// 기다렸다 가거나 바로가거나
						if (zero_point.front().time < Time) {
							Time += T;
						}
						else {
							Time = zero_point.front().time + T;
						}
					}
				}
			}
		}
	}

	cnt0 = 0;
	cnt1 = 0;
	for (auto i : order) {
		if (i) {
			cout << one_ans[cnt1].front() << " " << one_ans[cnt1].back() << '\n';
			cnt1++;
		}
		else {
			cout << zero_ans[cnt0].front() << " " << zero_ans[cnt0].back() << '\n';
			cnt0++;
		}
	}

	return 0;
}