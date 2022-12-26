from collections import deque

def bfs(i,j,c):
    q=deque()
    q.append((i,j,c))
    visit[i][j]=1
    while q:
        x,y,c=q.popleft()
        for ci,cj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+x,cj+y
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]==c and visit[ni][nj]==0:
                visit[ni][nj]=1
                q.append((ni,nj,c))
def bfs2(i,j):
    q=deque()
    q.append((i,j))
    visit[i][j]=1
    while q:
        x,y=q.popleft()
        for ci,cj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+x,cj+y
            if 0<=ni<N and 0<=nj<N :
                if arr[ni][nj]=='R' or arr[ni][nj]=='G':
                    if visit[ni][nj]==0:
                        visit[ni][nj]=1
                        q.append((ni,nj))

N=int(input())
arr=[input() for _ in range(N)]
visit=[[0]*N for _ in range(N)]
R=0
B=0
G=0
ans=[]
for i in range(N):
    for j in range(N):
        if arr[i][j]=='R' and visit[i][j]==0:
            bfs(i,j,'R')
            R+=1
        if arr[i][j]=='G' and visit[i][j]==0:
            bfs(i,j,'G')
            G+=1
        if arr[i][j]=='B' and visit[i][j]==0:
            bfs(i,j,'B')
            B+=1
ans.append((R+G+B))
R=0
visit=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]=='R' or arr[i][j]=='G':
            if visit[i][j]==0:
                bfs2(i,j)
                R+=1
ans.append(R+B)
print(*ans)