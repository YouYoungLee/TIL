from collections import deque

def isVisited(a1, b1):
    if visited[a1][b1] == 0:
        visited[a1][b1] = 1
        q.append([a1, b1])

def bfs():
    while q:
        a1, b1 = q.popleft()
        c1 = c - a1 - b1
        if a1 == 0:
            ans.append(c1)

        if a1 + b1 < b:  # a->b
            isVisited(0, a1 + b1)
        else:
            isVisited(a1-(b-b1), b)

        if a1 + c1 < c:  # a->c
            isVisited(0, b1)
        else:
            isVisited(a1 - (c - c1), b1)

        if a1 + b1 < a:  # b->a
            isVisited(a1 + b1, 0)
        else:
            isVisited(a, b1 - (a - a1))

        if c1 + b1 < c:  # b->c
            isVisited(a1, 0)
        else:
            isVisited(a1, b1 - (c - c1))

        if a1 + c1 < a:  # c->a
            isVisited(a1 + c1, b1)
        else:
            isVisited(a, b1)

        if c1 + b1 < b:  # c->b
            isVisited(a1, b1 + c1)
        else:
            isVisited(a1, b)

a,b,c = map(int, input().split())
MAX = 201
visited = [[0]* MAX for _ in range(MAX)]
visited[0][0] = 1

q = deque()
q.append([0, 0])  # 첫 번째, 두 번째 물병의 남은 용량을 표시

ans = []
bfs()
ans.sort()
print(' '.join(map(str, ans)))