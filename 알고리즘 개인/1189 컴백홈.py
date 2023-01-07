def bfs(x,y,d):
    global cnt
    if d==K:
        if x==0 and y==(C-1):
            cnt+=1
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni=x+di
        nj=y+dj
        if 0<=ni<R and 0<=nj<C and lst[ni][nj]!='T':
            lst[ni][nj]='T'
            bfs(ni,nj,(d+1))
            lst[ni][nj]='.'

R,C,K=map(int,input().split())
lst=[list(input())for _ in range(R)]
cnt=0
lst[(R-1)][0]='T'
bfs((R-1),0,1)
print(cnt)