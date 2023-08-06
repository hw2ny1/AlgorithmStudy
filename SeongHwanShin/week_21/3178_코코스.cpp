#include<iostream>
#include<algorithm>
#include<string>
#include<vector>

/*
문　제　3178_코코스
메모리　70804 KB
시　간　148 ms

트라이 구조를 사용해서 풀면 쉽게풀리는 문제이다.
문제에서 친절히 말해주듯 길이가 2K인데, K까지는 갈라지기, 2K까지는 합쳐지기가 되는데 여기서 기존 Trie구조를 사용할 시에 합쳐지는 부분은 구현이 어렵다.
따라서 그냥 1부터 K까지 저장하는 Trie하나, 2K부터 K+1까지 저장하는 Trie하나를 만들어 주면 된다.
여기서 unordered_map>>map>>vector 순으로 공간복잡도 차이가 생기므로
어느정도 시간복잡도를 감안하고 vector를 사용하여 메모리 문제를 해결할 수 있었다.
*/

using namespace std;

int N, K, ans;

// Trie에 사용될 노드
struct Trie {
	vector<pair<char, Trie*>> next;
}Node[1261817];

int cnt = 0;

// 새로운 정점을 반환
Trie* returnNode() {
	return &Node[cnt++];
}

// 2개의 Trie트리를 만듬
Trie trie_front = Trie();
Trie trie_back = Trie();

Trie* ret;
Trie* ret2;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> K;
	ans = 0;
	
	int flag;

	for (int i = 0; i < N; i++) {
		// 문자열을 입력받는다.
		string temp;
		cin >> temp;

		// 없으면 가지를 만들고 있으면 있는 가지로 이동
		ret = &trie_front;
		for (int i = 0; i < K; i++) {
			flag = 0;
			for (auto cur : ret->next) {
				if (cur.first == temp[i]) {
					flag = 1;
					ret = cur.second;
					break;
				}
			}
			if (!flag) {
				ret2 = returnNode();
				ret->next.push_back({ temp[i],ret2 });
				ret = ret2;
			}
		}
		
		// 굳이 string을 뒤집기 보다 뒤에서 참조하면 된다.
		ret = &trie_back;
		for (int i = 2*K-1; i >= K; i--) {
			flag = 0;
			for (auto cur : ret->next) {
				if (cur.first == temp[i]) {
					flag = 1;
					ret = cur.second;
					break;
				}
			}
			if (!flag) {
				ret2 = returnNode();
				ret->next.push_back({ temp[i],ret2 });
				ret = ret2;
			}
		}
	}

	// 새로운 노드를 반환한 수만큼이 결국 정점의 수
	cout << cnt;

	return 0;
}