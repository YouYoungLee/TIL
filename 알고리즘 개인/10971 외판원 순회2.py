n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
visit = [0] * n
m = 1e9
def dfs(depth, start, cost):
    global m
    if depth == n-1 and l[start][0] != 0:
        m = min(m, cost+l[start][0])
        return
    for i in range(n):
        if not visit[i] and l[start][i] != 0:
            visit[i] = 1
            dfs(depth+1, i, cost+l[start][i])
            visit[i] = 0
visit[0] = 1
dfs(0, 0, 0)
print(m)
