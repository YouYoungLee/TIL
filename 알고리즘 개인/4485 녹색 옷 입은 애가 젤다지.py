from collections import deque

i=1
while True:
    N=int(input())
    if N==0:
        break
    lst=[list(map(int,input().split())) for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visit = [[0] * N for _ in range(N)]
    visit[0][0] = lst[0][0]
    while q:
        x, y = q.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if visit[nx][ny] == 0:
                    q.append((nx, ny))
                    visit[nx][ny] = visit[x][y] + lst[nx][ny]
                else:
                    if visit[nx][ny] > visit[x][y] + lst[nx][ny]:
                        q.append((nx, ny))
                        visit[nx][ny] = visit[x][y] + lst[nx][ny]
    print("Problem {0}: {1}".format(i, visit[N-1][N-1]))
    i+=1

