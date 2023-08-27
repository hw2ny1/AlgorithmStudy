#include<iostream>

/*
문　제　19644_좀비_떼가_기관청_진지에도_오다니
메모리　25460 KB
시　간　372 ms
*/

using namespace std;

int N, len, damage, C;
unsigned int arr[3000001];
unsigned int psum[3000001];

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N;
	cin >> len >> damage;
	cin >> C;
	for (int i = 1; i <= N; i++) cin >> arr[i];
	for (int i = 1; i <= N; i++) {
		unsigned int now = psum[i - 1] - psum[max(0, i - len)];
		if (arr[i] <= now + damage) {
			psum[i] = psum[i - 1] + damage;
			continue;
		}
		else {
			if (C) {
				C--;
				psum[i] = psum[i - 1];
			}
			else {
				cout << "NO";
				return 0;
			}
		}
	}
	cout << "YES";
	return 0;
}