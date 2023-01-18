import sys
read = sys.stdin.readline

#유클리드 호제법을 사용해 최대공약수를 구한다.
def GCD(x, y):
    while y != 0:
        x, y = y, x % y
    return x


for _ in range(int(read())):
    n = int(read())
    num = list(map(int, read().split()))
    #밑에서 두 수의 차를 diff에 추가할 때, 음수가 나오지 않게 하기 위해서
    #정렬을 먼저 해주었다. 정렬을 하지 않고, 두 수의 차의 절대값을 diff에 추가해도 무방하다.
    num.sort()

    diff = set()
    for i in range(1, n):
        diff.add(num[i]-num[i-1])
    diff = list(diff)

    if diff == [0]:
        print('INFINITY')
        continue

    x = diff[0]
    for i in range(1, len(diff)):
        tmp = GCD(x, diff[i])
        x = tmp
    print(x)
