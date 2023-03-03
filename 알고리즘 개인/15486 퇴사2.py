import sys
input = sys.stdin.readline

# 입력
N = int(input())
consulting = []
for _ in range(N):
    consulting.append(list(map(int, input().split())))  # 시간, 가격

# DP
day = [0] * (N + 1)  # 해당 날짜에 최대로 받을 수 있는 돈
for i in range(N - 1, -1, -1):  # 마지막 날부터 첫 날까지 거슬러서 계산
    # N일을 벗어나는 스케줄은 무시
    if i + consulting[i][0] > N:
        day[i] = day[i + 1]

    # 해당 스케줄을 함으로써 더 돈을 많이 벌면 갱신
    else:
        day[i] = max(day[i + 1], day[i + consulting[i][0]] + consulting[i][1])
print(day[0])