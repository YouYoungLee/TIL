from collections import deque
def bfs():
    while f:
        x,y=f.popleft()
        for ci,cj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+x,cj+y
            if 0<=ni<R and 0<=nj<C and lst[ni][nj]!='#' and fvisit[ni][nj]==0:
                f.append((ni,nj))
                fvisit[ni][nj]=fvisit[x][y]+1
    while q:
        x,y=q.popleft()
        for ci,cj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+x,cj+y
            if 0<=ni<R and 0<=nj<C:
                if lst[ni][nj]!='#' and jvisit[ni][nj]==0:
                    if fvisit[ni][nj]==0 or fvisit[ni][nj] > jvisit[x][y] + 1:
                        q.append((ni,nj))
                        jvisit[ni][nj]=jvisit[x][y]+1
            else:
                return jvisit[x][y]
    return "IMPOSSIBLE"


R,C = map(int,input().split())
lst=[list(input()) for _ in range(R)]
jvisit=[[0]*C for _ in range(R)]
fvisit=[[0]*C for _ in range(R)]
f = deque()
q = deque()
for i in range(R):
    for j in range(C):
        if lst[i][j]=='J':
            ji,jj=i,j
            q.append((ji, jj))
            jvisit[ji][jj] = 1
        if lst[i][j]=='F':
            fi,fj=i,j
            f.append((fi, fj))
            fvisit[fi][fj] = 1


print(bfs())
