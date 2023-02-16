def dfs(n,st,lst,vo,co):
    if len(st)==L:
        if vo>=1 and co>=2:
            print(st)
        return
    if n==(C-1):
        return
    tempst=st+lst[n+1]
    if lst[n+1] in mo:
        dfs(n+1,tempst,lst,vo+1,co)
    else:
        dfs(n+1,tempst,lst,vo,co+1)
    dfs(n+1,st,lst,vo,co)

L,C=map(int,input().split())
lst=list(input().split())
lst.sort()
mo=['a','e','i','o','u']
if lst[0] in mo:
    dfs(0,lst[0],lst,1,0)
else:
    dfs(0,lst[0],lst,0,0)
dfs(0,"",lst,0,0)