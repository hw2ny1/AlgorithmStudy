"""
문　제　12904_A와B
메모리　33324 KB
시　간　48 ms

A와 B로만 구성된 문자열 S와 T가 있을 때, S로 T로 바꿀 수 있는지 구하는 문제

S를 T로 바꾸는 경우의 수보다 T를 S로 바꾸는 경우의 수가 적고
길이가 짧은 문자열을 우선적으로 처리하고 싶었기 때문에 heap 사용
문자열을 바꾸는 연산은 음수 인덱싱을 이용하여 구현
"""


from heapq import heappush as push
from heapq import heappop as pop

Word = input()
Target = input()
pq = [Target]
N = len(Word)
ans = 0

while pq:
    temp = pop(pq)
    if temp == Word:
        ans = 1
        break
    if len(temp) <= N:
        continue
    if temp[-1] == 'A':
        push(pq,temp[:-1])
    if temp[-1] == 'B':
        push(pq,temp[:-1][::-1])

print(ans)