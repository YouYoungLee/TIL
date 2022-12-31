from collections import deque

def bfs(i,j):
    q=deque()
    q.append((i,j))
    visit[i][j]=1
    while q:
        x,y=q.popleft()
        for ci,cj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+x,cj+y
            if 0<=ni<N and 0<=nj<M:
                if visit[ni][nj]==0 and lst[ni][nj]==1:
                    visit[ni][nj]=1
                    q.append((ni,nj))

T = int(input())
# T = 10
for test_case in range(1, T + 1):
    M,N,K=map(int,input().split())
    lst=[[0]*M for _ in range(N)]
    visit=[[0]*M for _ in range(N)]
    cnt=0
    for i in range(K):
        k,l=map(int,input().split())
        lst[l][k]=1
    for i in range(N):
        for j in range(M):
            if lst[i][j]==1 and visit[i][j]==0:
                bfs(i,j)
                cnt+=1
    print(cnt)