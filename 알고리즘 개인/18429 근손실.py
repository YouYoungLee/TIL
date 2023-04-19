def dfs(i,hp):
    global answer
    if hp<500:
        return
    if i>=N:
        answer+=1

    for j in range(N):
        if visit[j] == 0:
            visit[j] = 1
            dfs(i+1, hp+lst[j]-K)
            visit[j] = 0

N,K=map(int,input().split())
lst=list(map(int,input().split()))
visit=[0]*N
answer=0
dfs(0,500)
print(answer)