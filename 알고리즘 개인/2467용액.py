import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left = 0
right = N - 1
answer1 = 0
answer2 = 0
min_ = sys.maxsize
while left < right:

    total = arr[left] + arr[right]

    if abs(total) < min_:
        answer1 = arr[left]
        answer2 = arr[right]
        min_ = abs(total)

    if total < 0:
        left += 1

    elif total > 0:
        right -= 1
    else:
        break
print(answer1, answer2)
