import sys; input = sys.stdin.readline
from heapq import heappop, heappush
inf = 100000000 # 최대값 (max(N)-1) * max(w)
N = int(input()) # 1000
M = int(input()) # 100000
link_list = [list() for _ in range(N + 1)]
for _ in range(M):
    s, e, w = map(int,input().split())
    link_list[s].append((w, e))
    # link_list[e].append((w, s))
s, e = map(int, input().split())

dist = [inf for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]
dist[s] = 0
q = [(0, s)]
while q:
    w, cur = heappop(q)
    if visit[cur]: continue
    visit[cur] = True
    for adj_w, adj in link_list[cur]:
        if dist[adj] > adj_w + w:
            dist[adj] = adj_w + w
            heappush(q,(dist[adj], adj))

print(dist[e])