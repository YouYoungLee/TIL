def solution(x, y, d) :
    global result
    if data[x][y] == 0 :
        data[x][y] = 2
        result += 1
    for i in range(4) :
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if data[nx][ny] == 0 :
            solution(nx, ny, nd)
            return
        d = nd

    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if data[nx][ny] == 1 :
        return
    solution(nx, ny, d)

n, m = map(int, input().split())
r, c, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
solution(r, c, d)

print(result)