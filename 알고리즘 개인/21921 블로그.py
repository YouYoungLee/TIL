import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

tmp = sum(visitors[:X])
max_v = tmp
cnt = 1
for l in range(X, N):
    tmp -= visitors[l - X]
    tmp += visitors[l]
    if max_v < tmp:
        max_v = tmp
        cnt = 1
    elif max_v == tmp:
        cnt += 1
print("SAD") if max_v == 0 else print(max_v, cnt)