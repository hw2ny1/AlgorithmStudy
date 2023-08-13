import sys
input = sys.stdin.readline

N,R = map(int,input().split())
cities = list(input().rstrip().split()) # 모든 도시

M = int(input())
trip = list(input().rstrip().split()) # 여행 갈 도시

K = int(input())

INF = sys.maxsize
sale = [[INF]*N for _ in range(N)] # 내일로 구매 시 가격 정보
nonSale = [[INF]*N for _ in range(N)] # 내일로 미구매 가격 정보

for _ in range(K):
    info = list(input().rstrip().split())
    price = int(info[-1])
    a = cities.index(info[1])
    b = cities.index(info[2])

    # a -> b , b -> a 가격 정보 갱신

    # 내일로 아닐 때는 그냥 최소값 기입
    nonSale[a][b] = min(nonSale[a][b],price)
    nonSale[b][a] = min(nonSale[b][a],price)

    # 내일로 구매 시 조건에 따라 가격 변경해주고 최소값으로 갱신
    if info[0] in ['ITX-Saemaeul', 'ITX-Cheongchun','Mugunghwa'] :
        sale[a][b] = sale[b][a] = 0
    elif info[0] in ['S-Train','V-Train'] :
        sale[a][b] = min(sale[a][b],price/2)
        sale[b][a] = min(sale[b][a],price/2)
    else :
        sale[a][b] = min(sale[a][b],price)
        sale[b][a] = min(sale[b][a],price)

# 모든 점에 대해서 최소 값 갱신 ( 플로이드 워셜 )
def minPrice(lst) :
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i==j : continue
                lst[i][j] = min(lst[i][k] + lst[k][j], lst[i][j])

minPrice(nonSale)
minPrice(sale)

sale_price = 0
nonSale_price = 0
for i in range(M-1):
    a = cities.index(trip[i])
    b = cities.index(trip[i+1])

    # a에서 b 까지 가격 더하기
    sale_price += sale[a][b]
    nonSale_price += nonSale[a][b]

if sale_price + R < nonSale_price : print("Yes")
else : print("No")

