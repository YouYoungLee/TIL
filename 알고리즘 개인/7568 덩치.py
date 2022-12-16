N=int(inpN=int(input())
lst=[list(map(int,input().split())) for _ in range(N)]
answer=[]
for i in range(N):
    tmp=0
    for j in range(N):
        if lst[i][0]<lst[j][0]:
            if lst[i][1]<lst[j][1]:
                tmp+=1
    answer.append(tmp+1)
print(*answer)ut())
lst=[list(map(int,input().split())) for _ in range(N)]
answer=[]
for i in range(N):
    tmp=0
    for j in range(N):
        if lst[i][0]<lst[j][0]:
            if lst[i][1]<lst[j][1]:
                tmp+=1
    answer.append(tmp+1)
print(*answer)