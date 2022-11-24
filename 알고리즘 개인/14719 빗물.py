H,W = map(int,input().split())
lst = list(map(int,input().split()))

n=len(lst)
ma=max(lst)
mai=lst.index(ma)
temp=lst[0]
answer=0
for i in range(1,mai):
    if temp<=lst[i]:
        temp=lst[i]
        continue
    answer+=temp-lst[i]
temp=lst[n-1]
for i in range(n-2,mai,-1):
    if temp<=lst[i]:
        temp=lst[i]
        continue
    answer+=temp-lst[i]

print(answer)