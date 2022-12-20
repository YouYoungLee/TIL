N=int(input())
lst=list(map(int,input().split()))
M=int(input())
start=M//N
if sum(lst)<=M:
    print(max(lst))
else:
    while True:
        temp=0
        for i in range(N):
            if lst[i]>start:
                temp+=start
            else:
                temp+=lst[i]
        if temp<=M:
            maxi=start
            start+=1
        else:
            print(maxi)
            break
