def dfs(d):
    global answer
    global best
    if N<=d:
        best=max(best,answer)
        return
    dfs(d+1)
    if d+lst[d][0]<=N:
        answer+=lst[d][1]
        dfs(d+lst[d][0])
        answer-=lst[d][1]
N=int(input())
lst=[list(map(int,input().split())) for _ in range(N)]
answer=0
best=0
dfs(0)
print(best)