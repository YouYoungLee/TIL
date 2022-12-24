from collections import deque

def bfs(i,j,sm):
    global ans
    q=deque()
    q.append((i,j,sm))
    visit=[[0]*N for _ in range(N)]
    visit[i][j]=1
    while q:
        x,y,sm=q.popleft()
        if x==ei and y==ej:
            ans=sm
            break
        for ci,cj in ((2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)):
            ni,nj=ci+x,cj+y
            if 0<=ni<N and 0<=nj<N and visit[ni][nj]==0:
                visit[ni][nj]=1
                q.append((ni,nj,sm+1))

T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N=int(input())
    ans=0
    si,sj=map(int,input().split())
    ei,ej=map(int,input().split())
    bfs(si,sj,0)
    print(ans)