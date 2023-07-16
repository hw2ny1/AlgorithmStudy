#include<iostream>
#include<algorithm>
#include<queue>

#define MAX 99999999999

/*
문　제　2461_대표_선수
메모리　6144 KB
시　간　344 ms

각 반에서 대표를 선발하여 최대값과 최소값의 차이가 최소가 되는 경우를 구해야하는 문제이다.
따라서 각 반을 우선순위큐로 구현하고 능력치가 가장 큰 사람들부터 모아 최대-최소값을 구한다.
그리고 대표중에서 가장 큰사람을 제하고 그 반에서 그 다음으로 능력치가 큰사람을 불러와 최대-최소를 계속 갱신해나간다.
그러면 O(NM logM)으로 결과 값을 구할 수 있다.
*/

using namespace std;

// 반의 수와 학생의 수
int N, M, temp;
// 최소값을 저장
int Min = MAX;
// 결과 값을 저장
int result = MAX;
// 대표선수와 각반을 우선순위큐로 구현한다.
priority_queue<pair<int, int>>RepresentativePlayer;
priority_queue<int> Classmates[1001];

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> M;
	
	//각 반의 학생을 input받고 한명씩 대표로 선발한다(능력치가 제일 큰 사람)
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> temp;
			Classmates[i].push(temp);
		}
		temp = Classmates[i].top();
		Classmates[i].pop();
		RepresentativePlayer.push({ temp,i });
		Min = min(Min, temp);
	}

	// 대표선수 중에서 능력치가 가장 큰사람을 빼고 그 사람이 속한 반에서 새로 대표를 선발한다.
	while (true) {
		int Max = RepresentativePlayer.top().first;
		int Maxindex = RepresentativePlayer.top().second;
		RepresentativePlayer.pop();

		result = min(result, Max - Min);
		
		// 이과정에서 반의 인원이 더이상 없으면 break
		if (Classmates[Maxindex].empty()) break;

		// 최소값을 갱신해주고 대표선수에 넣는다.
		temp = Classmates[Maxindex].top();
		Classmates[Maxindex].pop();
		Min = min(Min, temp);
		RepresentativePlayer.push({ temp,Maxindex });
	}
	
	cout << result << endl;

	return 0;
}