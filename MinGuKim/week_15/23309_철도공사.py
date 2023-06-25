import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
ans = __pypy__.builders.StringBuilder()
n, m = map(int, input().split())
arr = list(map(int, input().split()))
station_prev = [0]*1000001
station_next = [0]*1000001
for i in range(n):
    station_prev[arr[i]] = arr[i - 1]
    station_next[arr[i - 1]] = arr[i]
for _ in range(m):
    order, *nums = input().split()
    if order[0] == 66:
        i, j = map(int, nums)
        if order[1] == 78:
            nex = station_next[i]
            ans.append(f"{nex}\n")
            station_next[j] = nex
            station_prev[j] = i
            station_next[i] = j
            station_prev[nex] = j
        else:
            pre = station_prev[i]
            ans.append(f"{pre}\n")
            station_next[j] = i
            station_prev[j] = pre
            station_prev[i] = j
            station_next[pre] = j
    else:
        i = int(nums[0])
        if order[1] == 78:
            pre, cur, nex = i, station_next[i], station_next[station_next[i]]
        else:
            pre, cur, nex = station_prev[station_prev[i]], station_prev[i], i
        station_next[pre] = nex
        station_prev[nex] = pre
        ans.append(f"{cur}\n")
os.write(1, ans.build().encode())