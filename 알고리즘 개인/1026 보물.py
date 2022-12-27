N=int(input())
lstA=list(map(int,input().split()))
lstB=list(map(int,input().split()))

answer=0
lstA.sort()
for i in range(N):
    x = lstA[i]
    y = lstB.pop(lstB.index(max(lstB)))

    answer +=x*y

print(answer)