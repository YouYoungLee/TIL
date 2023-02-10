def solution(x, y):
    if x == n-1 and y == n-1:
        return 1
    num = board[x][y]
    if dp[x][y] == -1:
        dp[x][y] = 0
        if 0<= x + num <n and 0 <= y < n:
            dp[x][y] += solution(x+num, y)
        if 0 <= x < n and 0 <= y + num < n:
            dp[x][y] += solution(x, y+num)
    return dp[x][y]

n = int(input())
dp = [[-1 for _ in range(n)] for _ in range(n)]
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
print(solution(0, 0))