from collections import deque

def bfs():
    q=deque()
    visit=[[0]*M for _ in range(N)]
    q.append((0,0))
    visit[0][0]=1
    while q:
        x,y=q.popleft()
        for ci,cj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+x,cj+y
            if 0<=ni<N and 0<=nj<M and visit[ni][nj]==0 and lst[ni][nj]==1:
                visit[ni][nj]=1
                lst[ni][nj]=0
            if 0<=ni<N and 0<=nj<M and visit[ni][nj]==0 and lst[ni][nj]==0:
                q.append((ni,nj))
                visit[ni][nj]=1


N,M = map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(N)]
cnt=0
ans=0
temp=[]
while True:
    for i in range(N):
        for j in range(M):
            if lst[i][j]==1:
                cnt+=1
    if cnt==0:
        break
    else:
        temp.append(cnt)
        cnt=0
        bfs()
        ans+=1
print(ans)
print(temp[ans-1])

