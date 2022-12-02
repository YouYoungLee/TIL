from itertools import combinations

N,M=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(N)]
house=[]
chicken=[]
ans=99999
for i in range(N):
    for j in range(N):
        if lst[i][j]==1:
            house.append([i,j])
        if lst[i][j]==2:
            chicken.append([i,j])
for chi in combinations(chicken,M):
    temp=0
    for h in house:
        chi_len = 999
        for j in range(M):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp+=chi_len
    ans=min(ans,temp)
print(ans)

