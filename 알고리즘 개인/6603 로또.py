import sys
input = sys.stdin.readline

def dfs(depth,i):
    if depth==6:
        print(*answer)
        return
    for j in range(i,N):
        answer.append(lst[j])
        dfs(depth+1,j+1)
        answer.pop()
while True:
    lst=list(map(int,input().split()))
    N=lst.pop(0)
    if not lst:
        break
    answer=[]
    dfs(0,0)
    print()