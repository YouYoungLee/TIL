from collections import deque
import copy
def dfs(cnt):
    if cnt==3:
        birus()
        return
    for i in range(N):
        for j in range(M):
            if lst[i][j]==0:
                lst[i][j]=1
                dfs(cnt+1)
                lst[i][j]=0
def birus():
    global answer
    count=0
    visited=copy.deepcopy(lst)
    for i in bixy:
        q.append(i)
    while q:
        x,y = q.popleft()
        for ci,cj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni=x+ci
            ny=y+cj
            if 0<=ni<N and 0<=ny<M and visited[ni][ny]==0:
                q.append((ni,ny))
                visited[ni][ny]=2
    for i in range(N):
        for j in range(M):
            if visited[i][j]==0:
                count+=1
    answer=max(count,answer)
N,M=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(N)]
q=deque()
bixy=[]
answer=0
for i in range(N):
    for j in range(M):
        if lst[i][j]==2:
            bixy.append((i,j))
dfs(0)
print(answer)