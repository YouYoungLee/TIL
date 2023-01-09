from collections import deque

m, n = map(int, input().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))
queue = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if tomato[nx][ny] == -1:
                continue
            if tomato[nx][ny] == 0:
                queue.append((nx, ny))
                tomato[nx][ny] = tomato[x][y] + 1

flag = False
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            flag = True
            break
if flag:
    print(-1)
else:
    print(max(map(max, tomato)) - 1)