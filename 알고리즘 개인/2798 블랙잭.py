def dfs(n,sm,cn):
    global ans
    if n==N:
        if sm>M:
            return
        if cn==3:
            ans=max(ans,sm)
        else:
            return
    if cn==3:
        if sm>M:
            return
        ans=max(ans,sm)
        return
    dfs(n+1,sm,cn)
    dfs(n+1,sm+lst[n],cn+1)
N,M=map(int,input().split())
lst=list(map(int,input().split()))
ans=0
dfs(0,0,0)
print(ans)