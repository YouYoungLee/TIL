from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001
q = deque([(n, 0)])
fastest, ways = 10 ** 6, 0

while q:
    now, time = q.popleft()
    visited[now] = True  # <- 방문 처리를 여기서 함
    if now == k and time <= fastest:
        fastest = min(fastest, time)
        ways += 1
    if time > fastest: break  # 큐에는 시간 순으로 들어가므로 fastest보다 커지면 탐색을 종료

    for x in (now - 1, now + 1, now * 2):
        if x in range(100001) and not visited[x]:
            q.append((x, time + 1))

print(fastest)
print(ways)