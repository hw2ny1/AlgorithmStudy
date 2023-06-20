#include<iostream>
#include<algorithm>
#include<string>
#include<map>
#include<set>

using namespace std;

/*
문　제　4797_화학식
메모리　2036 KB
시　간　0 ms

고정관념을 깨야 풀 수 있었던 파싱 문제
*/

// 화학식에서 구성하고 있는 원소의 갯수를 구해주는 API
void convert(string Molcular) {
	// 원소에 대한 갯수를 저장할 total[cnt] -> 괄호안에 들어가면 cnt가 올라간다.
	map<string, int>total[101];
	string temp = "";
	// set은 중복이 없고 자동으로 오름차순 정렬(사전순 정렬)을 해준다.
	set<string> names;
	// 괄호가 닫히고 분자가 몇개있는지 저장할 int 배열, 여러번 괄호를 들어가게 될 경우를 대비해서 분자단위로 몇개 있는지 기억해둔다.
	int merge[101];
	int cnt = 1;
	int k = 0; int n = 1; int z;

	fill_n(merge, 101, 1);

	while (k < Molcular.size()) {
		// 괄호가 열리면 cnt를 올려서 새로운 곳에 저장한다.
		if (Molcular[k] == '(') {
			cnt++;
			k++;
		}
		// 괄호가 닫히면 원소 갯수를 계산하여 cnt-1에 추합해준다.
		else if (Molcular[k] == ')') {
			k++;
			n = 1;
			// 여기서 n은 분자의 갯수가 된다.
			if (Molcular[k] > 47 && Molcular[k] < 58) n = (Molcular[k++] - 48);
			while (Molcular[k] > 47 && Molcular[k] < 58) {
				n *= 10;
				n += Molcular[k++] - 48;
			}
			merge[cnt] = n;

			// 각 원소를 순회하면서 cnt-1에다가 괄호안 원소갯수를 계산하여 더해준다.
			for (auto it = total[cnt].begin(); it != total[cnt].end(); it++) {
				temp = it->first;
				z = it->second * merge[cnt];
				total[cnt - 1][temp] += z;
			}
			// 초기화 해주지 않으면 다시 괄호가 들어갈 경우 데이터가 중복된다.
			total[cnt].clear();
			cnt--;
		}
		else {
			// 대문자와 소문자로 구분하여 화학식을 파싱한다.
			n = 1;
			temp = "";
			temp += Molcular[k++];
			while (Molcular[k] > 96) temp += Molcular[k++];
			if (Molcular[k] > 47 && Molcular[k] < 58) n = (Molcular[k++] - 48);
			while (Molcular[k] > 47 && Molcular[k] < 58) {
				n *= 10;
				n += Molcular[k++] - 48;
			}
			total[cnt][temp] += n;
			names.insert(temp);
		}
	}

	set<string>::iterator iter = names.begin();
	n = names.size();

	// 결과값 출력, 마지막에는 +가 붙지 않는다.
	for (int i = 0;i < n-1;i++) {
		if (total[1][*iter] != 1) cout << total[1][*iter];
		cout << *iter++ << '+';
	}
	if (total[1][*iter] != 1) cout << total[1][*iter];
	cout << *iter << '\n';
	return;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	string Molcular;

	// 더 이상 입력되는 화학식이 없으면 조건문에서 return하게 된다.
	while (true) {
		cin >> Molcular;
		if (Molcular == "0") return 0;
		convert(Molcular);
		Molcular = "0";
	}
}