#include<iostream>
#include<algorithm>
#include<set>
#include<string>
#include<vector>

/*
문　제　7432_디스크_트리
메모리　5596 KB
시　간　20 ms

directory라는 구조체를 만들어서 트라이구조를 구현했다.
*/

using namespace std;

int N;

struct directory {
	string name;
	bool end = false;
	int depth = -1;
	set<pair<string, directory*>> next;

	void insert(vector<string> lst, int index) {
		auto iter = next.begin();
		directory* next_directory;

		while (iter != next.end()) {
			if (iter->first == lst[index]) {
				next_directory = iter->second;
				break;
			}
			iter++;
		}
		
		if (iter == next.end()) {
			next_directory = new directory;
			next_directory->depth = index;
			next_directory->name = lst[index];
			next.insert({ lst[index],next_directory });
		}

		if (index == lst.size()-1) {
			next_directory->end = true;
			return;
		}

		next_directory->insert(lst, index + 1);
	}

	void print() {
		if (depth >= 0) {
			for (int i = 0; i < depth; i++) {
				cout << " ";
			}
			cout << name << '\n';
		}
		auto iter = next.begin();
		while (iter != next.end()) {
			iter->second->print();
			iter++;
		}
	}
} Directory;

directory* File_Directory = new directory;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N;

	string temp, path;

	for (int i = 0; i < N; i++) {
		vector<string> file_list;
		cin >> temp;
		int j = 0;
		int k = 0;
		path = "";
		
		while (j < temp.size()) {
			if (temp[j] == '\\'){
				file_list.push_back(path);
				path = "";
				j++;
				continue;
			}
			path.push_back(temp[j++]);
		}
		file_list.push_back(path);

		File_Directory->insert(file_list, 0);
	}

	File_Directory->print();
	return 0;
}