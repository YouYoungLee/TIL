from collections import deque
def bfs(i,j):
    global answer
    visit=[[0]*W for _ in range(L)]
    q=deque()
    visit[i][j]=1
    q.append((i,j,0))
    while q:
        x,y,cnt=q.popleft()
        for cx,cy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx=cx+x
            ny=cy+y
            if 0<=nx<L and 0<=ny<W and lst[nx][ny]=='L' and visit[nx][ny]==0:
                answer = max(answer, cnt)
                visit[nx][ny]=1
                q.append((nx,ny,cnt+1))

L,W=map(int,input().split())
lst=[list(input()) for _ in range(L)]
answer=0
for i in range(L):
    for j in range(W):
        if lst[i][j]=='L':
            bfs(i,j)
print(answer+1)