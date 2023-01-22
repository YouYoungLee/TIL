def bing(i,j):
    cnt=0
    for ci,cj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj=ci+i,cj+j
        if 0<=ni<N and 0<=nj<M and lst[ni][nj]==0:
            cnt+=1
    return cnt
def count_iceberg(i,j):
    q=[]
    q.append((i,j))
    visited[i][j]=1
    while q:
        ci,cj=q.pop(0)
        for si,sj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+si,cj+sj
            if 0<=ni<N and 0<=nj<M and lst2[ni][nj]!=0 and visited[ni][nj]==0:
                visited[ni][nj]=1
                q.append((ni,nj))
N,M=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(N)]
lst2=[[0]*M for _ in range(N)]
year=0

while True:
    visited=[[0]*M for _ in range(N)]
    piece=0
    flag=1
    for i in range(N):
        for j in range(M):
            if lst[i][j]!=0:
                flag=0
    if flag==1:
        print(0)
        break
    for i in range(N):
        for j in range(M):
            if lst[i][j]!=0:
                temp=bing(i,j)
                if lst[i][j]-temp<=0:
                    lst2[i][j]=0
                else:
                    lst2[i][j]=lst[i][j]-temp
    year+=1
    for i in range(1,N-1):
        for j in range(1,M-1):
            if visited[i][j]==0 and lst2[i][j]!=0:
                count_iceberg(i,j)
                piece+=1
    if piece>=2:
        print(year)
        break
    else:
        lst=lst2
        lst2 = [[0] * M for _ in range(N)]
