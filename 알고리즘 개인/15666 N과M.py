n, m = map(int, input().split())
k = sorted(set(list(map(int, input().split()))))
ans = []
p = []
def solve(depth, idx):
    if depth == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(idx, len(k)):
        ans.append(k[i])
        solve(depth+1, i)
        ans.pop()

solve(0, 0)
p = sorted(list(set(p)))