#include<iostream>
#include<vector>
#include<queue>

using namespace std;

/*
문　제　17299_오등큰수
메모리　14000 KB
시　간　804 ms

생각보다 시간이 많이 나왔다.
아마 stack을 쓰지않고 vector를 써서 동적 메모리 할당에 시간이 많이 쓰인건가? 로직은 비슷한 것 같다.

라고 생각했으나 그냥 cin의 stdio동기화를 끄지 않아서 그런거였다.
*/

int arr[1000002];
int NGF[1000002] = { 0 };
vector<int> stack;
deque<int> ans;

int main() {
	int N;
	cin >> N;

	for (int i = 1; i <= N; i++) {
		cin >> arr[i];
		NGF[arr[i]]++;
	}

	while (N) {
		while (stack.size() && NGF[stack.back()] <= NGF[arr[N]]) {
			stack.pop_back();
		}

		if (stack.empty()) {
			ans.push_front(-1);
		}
		else {
			ans.push_front(stack.back());
		}

		stack.push_back(arr[N--]);
	}

	for (auto i : ans) {
		cout << i << ' ';
	}
	return 0;
}