#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
#define endl '\n'

/*
문　제　23309_철도_공사
메모리　25464 KB
시　간　1088 ms

이전역과 이후역을 참조해야하므로 double-linkedlist를 구성하여 해결하려 했다.
linkedlist같은 경우 랜덤액세스가 O(N)이기 때문에, 각 id에 해당하는 주소를 hash로 저장해 두려고 했다.
그렇게 풀이한 결과 | 메모리 68064 KB | 시간 1876 ms | 로 해결할 수 있었다.
그러나 생각해보니 노드를 100만개 만들어 두었고 생성할 때도 id값에 해당하는 node를 사용하고 있기 때문에,
hash를 사용할 필요가 없었고 그냥 node[id]로 호출하면 된다는 것을 깨달았다.
그 부분을 반영한 결과 | 메모리 25464 KB | 시간 1088 ms | 로 해결할 수 있었다.
*/

using namespace std;

// 연결리스트에 사용될 노드를 미리 만들어둔다. ID가 최대 100만까지라 했으므로 100만개 이상 생성
// 주어진 API에 이전 역과 이후 역을 참조해야 하므로 double linkedlist 구성
struct Node {
	int id;
	Node* prev;
	Node* next;
}node[1000013];

struct Station {
	Node* head;
	Node* tail;

	// 주어진 id의 노드를 반환해주는 함수. 근데 이것도 사실 필요 없긴하다.
	Node* getNewNode(int id) {
		Node* ret = &node[id];
		ret->id = id;
		ret->prev = nullptr;
		ret->next = nullptr;
		return ret;
	}

	// i역 다음역의 고유번호 출력하고 사이에 j인 역 설립
	void BN(int i, int j) {
		// 고유번호 출력
		cout << node[i].next->id << endl;

		// 사이에 j인 역 설립하는 과정
		Node* ret = getNewNode(j);

		node[i].next->prev = ret;
		ret->next = node[i].next;

		ret->prev = &node[i];
		node[i].next = ret;
	}

	// i역 이전역의 고유번호를 출력하고 사이에 j인 역 설립
	void BP(int i, int j) {
		// 고유번호 출력
		cout << node[i].prev->id << endl;

		// 사이에 j인 역 설립하는 과정
		Node* ret = getNewNode(j);

		node[i].prev->next = ret;
		ret->next = &node[i];

		ret->prev = node[i].prev;
		node[i].prev = ret;
	}

	// i역 다음역을 폐쇄하고 그 역의 고유번호 출력
	void CN(int i) {
		// 고유번호 출력
		cout << node[i].next->id << endl;

		// 다음역 폐쇄하는 과정
		Node* ret = node[i].next;
		
		ret->next->prev = &node[i];
		node[i].next = ret->next;
	}

	// i역 이전역을 폐쇄하고 그 역의 고유번호 출력
	void CP(int i) {
		// 고유번호 출력
		cout << node[i].prev->id << endl;

		// 다음역 폐쇄하는 과정
		Node* ret = node[i].prev;

		ret->prev->next = &node[i];
		node[i].prev = ret->prev;
	}
}station;

// N: 역의 개수, M: 공사횟수
int N, M;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> M;
	
	int temp, i, j;
	string select;
	station.head = nullptr;

	// 처음 역 상태를 초기화 하는 과정
	for (int i = 0; i < N; i++) {
		if (station.head != nullptr) {
			cin >> temp;
			Node* stain = station.getNewNode(temp);

			stain->prev = station.tail;
			station.tail->next = stain;
			station.tail = stain;
		}
		else {
			cin >> temp;
			station.head = station.getNewNode(temp);
			station.head->next = station.head;
			station.head->prev = station.head;
			station.tail = station.head;
		}
	}

	station.tail->next = station.head;
	station.head->prev = station.tail;

	// M번 동안 공사 정보에 따라 API 호출
	while (M--) {
		cin >> select;
		if (select == "BN") {
			cin >> i >> j;
			station.BN(i, j);
		}
		else if (select == "BP") {
			cin >> i >> j;
			station.BP(i, j);
		}
		else if (select == "CN") {
			cin >> i;
			station.CN(i);
		}
		else if (select == "CP") {
			cin >> i;
			station.CP(i);
		}
	}

	return 0;
}