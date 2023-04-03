N=int(input())
lst=list(map(int,input().split()))
B,C=map(int,input().split())
result=N
for i in lst:
    i-=B
    if i>0:
        if i%C:
            result+=(i//C)+1
        else:
            result+=(i//C)
print(result)