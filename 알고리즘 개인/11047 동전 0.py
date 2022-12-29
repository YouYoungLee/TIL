N,K=map(int,input().split())
dong=[]
answer=0
for i in range(N):
    temp=int(input())
    dong.append(temp)
while True:
    for i in range((N-1),-1,-1):
        if dong[i]<=K:
            K=K-dong[i]
            answer+=1
            break
    if K==0:
        break
print(answer)
