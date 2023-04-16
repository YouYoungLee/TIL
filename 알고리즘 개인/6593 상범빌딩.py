from collections import deque
def bfs(start):
    q.append(start)
    visit[start[0]][start[1]][start[2]]=1
    switch=0
    while q:
        z,x,y,cnt=q.popleft()
        for cz,cx,cy in ((0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(1,0,0),(-1,0,0)):
            nz=z+cz
            nx=x+cx
            ny=y+cy
            if 0<=nz<L and 0<=nx<R and 0<=ny<C and visit[nz][nx][ny]==0:
                if lst[nz][nx][ny]=='.':
                    q.append((nz,nx,ny,cnt+1))
                    visit[nz][nx][ny]=1
                elif lst[nz][nx][ny]=='E':
                    print(f'Escaped in {cnt+1} minute(s).')
                    switch = 1
                    break
        if switch==1:
            break
    if switch==0:
        print('Trapped!')
while True:
    L,R,C = map(int,input().split())
    if L==0:
        break
    lst = [[[] * C for _ in range(R)] for _ in range(L)]
    visit = [[[0] * C for _ in range(R)] for _ in range(L)]
    q=deque()
    for i in range(L):
        lst[i]=[list(input()) for _ in range(R)]
        input()
    for i in range(L):
        for j in range(R):
            for v in range(C):
                if lst[i][j][v]=='S':
                    start=(i,j,v,0)
    bfs(start)
