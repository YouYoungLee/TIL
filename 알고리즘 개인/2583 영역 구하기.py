from collections import deque
def bfs(i,j):
    q=deque()
    visit[i][j]=1
    q.append((i,j))
    count=1
    while q:
        x,y=q.popleft()
        for ci,cj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=x+ci,y+cj
            if 0<=ni<M and 0<=nj<N and visit[ni][nj]==0 and lst[ni][nj]==0:
                visit[ni][nj]=1
                q.append((ni,nj))
                count+=1
    return count
M,N,K=map(int,input().split())
lst=[[0]*N for _ in range(M)]
ans=[]
for i in range(K):
    temp=list(map(int,input().split()))
    for i in range(temp[1],temp[3]):
        for j in range(temp[0],temp[2]):
            lst[(M-i-1)][j]=1
visit=[[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if lst[i][j]==0 and visit[i][j]==0:
            ans.append(bfs(i,j))
ans.sort()
print(len(ans))
print(*ans)
