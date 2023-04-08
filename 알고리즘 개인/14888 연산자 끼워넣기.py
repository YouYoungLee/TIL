def dfs(i,result):
    global answerMax,answerMin
    if i==(N-1):
        answerMax=max(answerMax,result)
        answerMin=min(answerMin,result)
        return
    if i==0:
        if yun[0]>0:
            yun[0]-=1
            dfs(i+1,lst[i]+lst[i+1])
            yun[0]+=1
        if yun[1]>0:
            yun[1]-=1
            dfs(i+1,lst[i]-lst[i+1])
            yun[1]+=1
        if yun[2]>0:
            yun[2]-=1
            dfs(i+1,lst[i]*lst[i+1])
            yun[2]+=1
        if yun[3]>0:
            yun[3]-=1
            dfs(i+1,lst[i]//lst[i+1])
            yun[3]+=1
    else:
        if yun[0]>0:
            yun[0]-=1
            dfs(i+1,result+lst[i+1])
            yun[0]+=1
        if yun[1]>0:
            yun[1]-=1
            dfs(i+1,result-lst[i+1])
            yun[1]+=1
        if yun[2]>0:
            yun[2]-=1
            dfs(i+1,result*lst[i+1])
            yun[2]+=1
        if yun[3]>0:
            yun[3]-=1
            if result<0:
                dfs(i+1,-(-result//lst[i+1]))
            else:
                dfs(i+1,result//lst[i+1])
            yun[3]+=1



N=int(input())
lst=list(map(int,input().split()))
yun=list(map(int,input().split()))
answerMax=-1e9
answerMin=1000000000
dfs(0,0)
print(answerMax)
print(answerMin)