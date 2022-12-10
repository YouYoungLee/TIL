X = int(input())
# memoization을 위한 초기화
cache = [0 for i in range(X+1)]
# dynamic programming 진행
for i in range(2, X+1):
  # 1빼는 연산
  cache[i] = cache[i-1]+1
  # 현재 수가 2로 나누어질때
  if i%2==0:
    cache[i] = min(cache[i], cache[i//2]+1)
  # 현재 수가 3으로 나누어질때
  if i%3==0:
    cache[i] = min(cache[i], cache[i//3]+1)

print(cache[X])