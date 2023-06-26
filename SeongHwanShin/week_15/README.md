:memo: 문제 -  :exclamation: 코멘트

- 영록
- 
가스관 문제에서 search 함수의 while문에서 델타 탐색을 할때 if arr[x][y] == '|' : 이런식으로 하나하나 해주는 것 보다 if arr[x][y] != 'M' and arr[x][y] != 'Z' and arr[x][y] != '.' : 으로 해두고 for ddx, ddy in veiw[arr[x][y]] : 이렇게 했으면 코드 길이가 많이 줄어들 것 같습니다.
