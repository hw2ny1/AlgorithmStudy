import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

visited = [0]*(max(lst)+1)  # 숫자가 몇번 나왔는지 저장할 리스트 인덱스가 그 숫자
for i in lst :
    visited[i] += 1 # 숫자가 나올때마다 visited +1씩 해줌

st = [] # st에는 오등큰수를 조사할 인덱스가 들어간다.
ans = [0]*(n) # 오등큰수 정보 저장할 리스트

for i in range(n):
    while st and visited[lst[st[-1]]] < visited[lst[i]] :
        #만약 현재 조사하는 인덱스의 lst값이 st[-1]에 있는 인덱스의 lst 보다 많이 있다면
        #st[-1]의 오등큰수는 lst[i]
        ans[st.pop()] = lst[i]
    st.append(i)

for num in st : # 마지막까지 남아있는애들은 오등큰수가 없다.
    ans[num] = -1

print(*ans)