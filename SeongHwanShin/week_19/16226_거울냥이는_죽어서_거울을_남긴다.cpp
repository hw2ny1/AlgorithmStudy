#include<iostream>
#include<algorithm>
#include<queue>
#include<vector>

/*
문　제　16226_거울냥이는_죽어서_거울을_남긴다
메모리　30324 KB
시　간　68 ms

row와 col이 최대 20만까지 될 수 있으므로 array로는 해결하지 못하므로 linkedlist를 사용하고 좌표압축을 이용하기로 했다.
처음에는 행도 연결해주어서 2차원 연결 리스트로 상하좌우의 주소를 각 노드마다 저장하였지만, 문제 특성상 행만 생각하면 되었다.
따라서 double linked list를 행 갯수만큼 만들어 주었으며 처음에는 O(n)으로 노드를 삽입하였으나 생각해보니 1행에만 노드를 20만개 넣을 경우, 20만*20만/2 이므로 시간초과가 날 수 있다.
그러므로 처음에 모든 input을 저장한 뒤 정렬을 해주면 O(N log N)의 시간복잡도가 걸리지만, 순서대로 삽입하면 되므로 노드삽입에 O(1)이 되어 문제를 해결할 수 있었다.
*/

using namespace std;

// 냥이 마리수
int N;

// 냥이는 0번부터 저장해요
int cat_cnt = 0;

// 거울은 20만번부터 저장해요
int cnt = 200322;

// 정답 = 냥이 마리수 - 죽은 냥이수
int ans;

// 처음에 좌표순서대로 정렬하기 위해 데이터를 저장한다.
typedef struct piii {
	int x;
	int y;
	bool type;

	piii(int a, int b, bool c) : x(a), y(b), type(c) {};
};

// pq비교 함수
struct compare {
	bool operator()(piii a, piii b){
		if (a.x != b.x) return a.x > b.x;
		if (a.y != b.y) return a.y > b.y;
		return true;
	}
};

// 좌표를 오름차순으로 정렬한다.
priority_queue<piii,vector<piii>,compare> pq;

// cm == 1 -> 냥이, cm == 0 -> 거울
struct Node {
	bool cm;
	int x;
	int y;
	Node* left;
	Node* right;
} node[704044];

// 냥이 노드 반환, 거울 노드 반환
Node* getNewNode(int x, int y, bool catmirror) {
	if (catmirror) {
		Node* ret = &node[cat_cnt++];
		ret->cm = catmirror;
		ret->x = x;
		ret->y = y;
		return ret;
	}
	else {
		Node* ret = &node[cnt++];
		ret->cm = catmirror;
		ret->x = x;
		ret->y = y;
		return ret;
	}
}

// 행마다 head와 back을 저장
struct Lattic {
	Node* node;
	Node* back;
} lattice[100010];

// 격자판에 거울 혹은 냥이를 놓는 함수 (push_back)
void insert(Node* ret) {
	Node* row = lattice[ret->x].back;
	row->right = ret;
	ret->left = row;
	lattice[ret->x].back = ret;
}

// 좌우로 레이저를 발사한다. 거울을 만날 때 까지 냥이를 죽인다.... 냥이가 죽으면 ans가 감소한다.
void LaserBeam(Node node) {
	Node* ret = node.left;
	while (ret->cm) {
		ret->cm = 0;

		ret->right->left = ret->left;
		ret->left->right = ret->right;

		ret = ret->left;
		ans--;
	}

	ret = node.right;
	while (ret->cm) {
		ret->cm = 0;

		ret->right->left = ret->left;
		ret->left->right = ret->right;

		ret = ret->right;
		ans--;
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N;

	ans = N;
	Node* ret;

	// head 노드
	for (int i = 0; i < 100003; i++) {
		lattice[i].node = getNewNode(i, 0, false);
		lattice[i].back = lattice[i].node;
	}

	// 좌표를 input받고 정렬한다.
	int a, b;
	for (int i = 0; i < N; i++) {
		cin >> a >> b;
		pq.push(piii(a++, b, true));
		pq.push(piii(a, b, false));
	}
	
	// 좌표 순서대로 insert하므로 O(1)로 linkedlist를 만들 수 있다.
	while (!pq.empty()) {
		piii temp = pq.top();
		pq.pop();

		insert(getNewNode(temp.x, temp.y, temp.type));
	}

	// back에 더미노드를 넣는다. 따라서 냥이 앞과 뒤에 경계를 만든다.
	for (int i = 0; i < 100003; i++) {
		ret = getNewNode(i, 100055, false);

		lattice[i].back->right = ret;
		ret->left = lattice[i].back;
		lattice[i].back = ret;
	}

	// 순서대로 냥이가 살아있으면 좌우로 레이저를 쏜다.
	for (int i = 0; i < N; i++) {
		if (node[i].cm) {
			LaserBeam(node[i]);
		}
	}

	// 정답 출력
	cout << ans;

	return 0;
}