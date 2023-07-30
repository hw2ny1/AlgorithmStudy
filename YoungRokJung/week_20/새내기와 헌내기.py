import sys

sys.setrecursionlimit(10**8)

def dfs(si, siColor):
    global n,link,visit,type
    visit[si]=True
    type[si]=siColor
    typeCnt=[0,0]
    typeCnt[type[si]]+=1

    for i in range(1,n+1):
        if link[si][i]=="1" and not visit[i]:
            x,y=dfs(i, (siColor + 1) % 2)
            typeCnt[0]+=x
            typeCnt[1]+=y

    return typeCnt

n=int(input())
link=[["0" for i in range(n+2)]]
for i in range(n):
    lst = input()
    link.append(["0", *list(lst), "0"])
link.append(["0" for i in range(n+2)])

for i in range(1,n+1):
    for j in range(1,n+1):
        if link[i][j]=="1":
            link[j][i]="1"
            pass

# print(link)
visit=[0]*(n+2) # 각 행 방문 여부
type=[0]*(n+2) # 각 행의 타입

ans=0
for i in range(1,n+1):
    if not visit[i]:
        ans+=max(dfs(i,0))
print(ans)