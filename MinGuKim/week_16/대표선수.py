import heapq

N, M = map(int, input().split())
arr = []
ind = [1] * 1001
maxVal = 0
hq = []
for i in range(N):
    li = list(map(int, input().split())) # 각 줄 list를 입력받음
    li.sort() # list를 정렬
    maxVal = max(maxVal, li[0]) # list의 첫번째 값과 maxVal 중 더 큰 값을 저장
    arr.append(li) # list를 arr에 추가
    heapq.heappush(hq, (arr[i][0], i)) # 최소 힙 hq에 리스트의 최소값과 인덱스를 푸시

# 이 과정이 끝나게 되면 maxVal에는 각 줄의 첫번째 값 중 가장 큰 값이 있게 되는데,
# 각 줄의 첫번째 값이 각 줄의 최소값이므로 이 중 최대값을 구하는 것은 중요함

res = 10**9
while hq: # hq가 빌 때까지
    front = heapq.heappop(hq) # hq에 푸쉬된 값 중 가장 작은 값을 front에 저장
    minVal = front[0]
    index = front[1]

    res = min(res, maxVal - minVal) # 배열에 선택된 값 중 최대값과 최소값의 차이와 res 값 중 더 작은 것을 저장
    if ind[index] == M: # 만약 M개가 모두 선택되었으면 종료
        break
    heapq.heappush(hq, (arr[index][ind[index]], index)) # hq에서 다음으로 작은 값을 푸쉬
    maxVal = max(maxVal, arr[index][ind[index]]) # maxVal이 바뀐다면 maxVal을 저장
    ind[index] += 1

print(res)
# 모든 배열에 대하여 체크한 뒤 최종 res 값을 출력