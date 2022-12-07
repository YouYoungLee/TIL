from collections import deque

def solve():
    while q:
        i,j,b,t=q.popleft()
        if t==S:
            break
        for si,sj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=si+i,sj+j
            if 0<=ni<N and 0<=nj<N and lst[ni][nj]==0:
                lst[ni][nj]=b
                q.append((ni,nj,b,t+1))


N,K=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(N)]
S,X,Y=map(int,input().split())
q=deque()
for n in range(1,K+1):
    for i in range(N):
        for j in range(N):
            if lst[i][j]==n:
                q.append((i,j,n,0))
solve()
print(lst[X-1][Y-1])


