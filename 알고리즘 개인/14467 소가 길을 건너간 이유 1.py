N=int(input())
lst=[3]*11
answer=0
for _ in range(N):
    L,M=map(int,input().split())
    if lst[L]==3:
        lst[L]=M
    else:
        if lst[L]==M:
            continue
        else:
            lst[L]=M
            answer+=1
print(answer)
