from collections import deque

def bfs(n,t):
    global ans
    q=deque()
    q.append((n,t))
    visit=[100005]*100005
    visit[n]=t
    while q:
        x,s = q.popleft()

        nx = 2 * x
        if 0 <= nx <= 100002 and visit[nx]==100005:
            q.append((nx, s))
            visit[nx] = s

        for nx in ((x-1),(x+1)):
            if 0<=nx<=100002 and visit[nx]==100005:
                q.append((nx,s+1))
                visit[nx]=s+1
    return visit[K]
N,K=map(int,input().split())
ans=1000000
a=bfs(N,0)
print(a)