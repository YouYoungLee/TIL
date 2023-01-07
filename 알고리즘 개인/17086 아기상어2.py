
from collections import deque

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visit=[[0]*M for _ in range(N)]
    visit[x][y]=1
    while q:
        i,j=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
            ni=i+di
            nj=j+dj
            if 0<=ni<N and 0<=nj<M and visit[ni][nj]==0:
                visit[ni][nj]=1
                q.append((ni,nj))
                if lst[ni][nj]==0:
                    lst[ni][nj]=(lst[i][j]+1)
                else:
                    if lst[ni][nj]>(lst[i][j]+1):
                        lst[ni][nj]=(lst[i][j]+1)

N,M=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if lst[i][j]==1:
            bfs(i,j)
tmpmax=0
for i in range(N):
    tmpmax=max(max(lst[i]),tmpmax)
print(tmpmax-1)