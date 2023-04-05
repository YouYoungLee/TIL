from collections import deque
def mise(i,j):
    count=0
    for ci,cj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni=ci+i
        nj=cj+j
        if 0<=ni<R and 0<=nj<C and lst[ni][nj]!=-1:
            tmp[ni][nj]+=lst[i][j]//5
            count+=1
    tmp[i][j]+=lst[i][j]-(lst[i][j]//5)*count
def upair():
    q.append((air,1,lst[air][1]))
    lst[air][1]=0
    while q:
        for ci,cj in ((0,1),(-1,0),(0,-1),(1,0)):
            while True:
                x, y,c = q.popleft()
                ni=x+ci
                nj=y+cj
                if ni<0 or ni>=R or nj<0 or nj>=C:
                    q.append((x,y,c))
                    break
                else:
                    if lst[ni][nj] == -1:
                        break
                    q.append((ni,nj,lst[ni][nj]))
                    lst[ni][nj]=c
def downair():
    q.append(((air+1),1,lst[air+1][1]))
    lst[air+1][1]=0
    while q:
        for ci,cj in ((0,1),(1,0),(0,-1),(-1,0)):
            while True:
                x, y,c = q.popleft()
                ni=x+ci
                nj=y+cj
                if ni<0 or ni>=R or nj<0 or nj>=C:
                    q.append((x,y,c))
                    break
                else:
                    if lst[ni][nj] == -1:
                        break
                    q.append((ni,nj,lst[ni][nj]))
                    lst[ni][nj]=c
R,C,T=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(R)]
q=deque()
air=-3
for _ in range(T):
    tmp=[[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if lst[i][j]>0:
                mise(i,j)
            if lst[i][j]==-1:
                if air==-3:
                    air=i
                tmp[i][j]=-1
    lst=tmp.copy()
    upair()
    downair()
result=0
for i in range(R):
    result+=sum(lst[i])
print(result+2)

