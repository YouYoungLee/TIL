from collections import deque

def bfs(i,j):
    q=deque()
    q.append((i,j))
    visited[i][j]=0
    while q:
        x,y=q.popleft()
        for ci,cj in ((-1,0),(1,0),(0,-1),(0,1)):
            nx=x+ci
            ny=cj+y
            if 0<=nx<N and 0<=ny<M and lst[nx][ny]==1 and visited[nx][ny]==0:
                visited[nx][ny]+=visited[x][y]+1
                q.append((nx,ny))
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and lst[i][j] == 1:
                visited[i][j] = -1



N,M=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if lst[i][j]==2:
            bfs(i,j)


for i in range(N):
    print(*visited[i])
