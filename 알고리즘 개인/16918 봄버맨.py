from collections import deque

R, C, N = map(int,input().split())

bomb = []
for i in range(R):
    row = input()
    bomb.append(list(row))

# print(bomb)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def counting_bomb():
    for i in range(R):
        for j in range(C):
            if bomb[i][j] == 'O':
                bomb_queue.append([i, j])

def deploy_bomb():
    for i in range(R):
        for j in range(C):
            bomb[i][j] = 'O'

def exploding_bomb():
    while bomb_queue:
        now = bomb_queue.popleft()
        x = now[0]
        y = now[1]
        bomb[x][y] = '.'
        for dir in range(4):
            nx = x+dx[dir]
            ny = y+dy[dir]
            if 0<=nx<R and 0<=ny<C:
                bomb[nx][ny] = '.'

N -= 1
while N>0:
    bomb_queue = deque()
    counting_bomb() # 설치된 폭탄들을 기록한다
    deploy_bomb()   # 폭탄을 설치한다
    N -= 1          # 1초 경과
    if N == 0:      # 시간이 다 됐나?
        break
    exploding_bomb()    # 터진다
    N -= 1

for i in bomb:
    print(''.join(i))