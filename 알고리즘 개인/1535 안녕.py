def dfs(n,hp,sm):
    global ans
    if hp<=0:
        return
    ans=max(ans,sm)
    if n==N:
        return




    dfs(n+1,hp-l[n],sm+j[n])
    dfs(n+1,hp,sm)



N=int(input())
l=list(map(int,input().split()))
j=list(map(int,input().split()))
ans=0
dfs(0,100,0)
print(ans)
