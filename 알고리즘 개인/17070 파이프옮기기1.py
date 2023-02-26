import sys
count = 0
N = int(input())
home = []

for _ in range(N):
    home.append([int(x) for x in sys.stdin.readline().rstrip().split()])

def dfs(x,y,state): # state 0: 가로, 1: 세로 , 2: 대각선
    global count
    if x == N - 1 and y == N - 1:
        count += 1
        return

    if state == 0:
        if y == N - 1: # 이동불가
            return

        if 0 <= x < N and 0 <= y + 1 < N and home[x][y + 1] == 0:
            dfs(x, y + 1, 0)

        if 0 <= x + 1 < N and 0 <= y + 1 < N and home[x][y + 1] == 0 and home[x + 1][y] == 0 and home[x + 1][
            y + 1] == 0:
            dfs(x + 1, y + 1, 2)

    elif state == 1:
        if x == N - 1: # 이동불가
            return

        if 0 <= x + 1 < N and 0 <= y < N and home[x + 1][y] == 0:
            dfs(x + 1, y, 1)

        if 0 <= x + 1 < N and 0 <= y + 1 < N and home[x][y + 1] == 0 and home[x + 1][y] == 0 and home[x + 1][
            y + 1] == 0:
            dfs(x + 1, y + 1, 2)

    elif state == 2:
        if 0 <= x < N and 0 <= y + 1 < N and home[x][y + 1] == 0:
            dfs(x, y + 1, 0)

        if 0 <= x + 1 < N and 0 <= y < N and home[x + 1][y] == 0:
            dfs(x + 1, y, 1)

        if 0 <= x + 1 < N and 0 <= y + 1 < N and home[x][y + 1] == 0 and home[x + 1][y] == 0 and home[x + 1][
            y + 1] == 0:
            dfs(x + 1, y + 1, 2)

dfs(0,1,0)
print(count)