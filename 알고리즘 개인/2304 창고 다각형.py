N=int(input())
lst=[]
temp=0
maxre=0
maxin=0
for _ in range(N):
    a,b=map(int,input().split())
    temp=max(temp,a)
    if maxre<=b:
        maxre=b
        maxin=a
    lst.append((a,b))
lst2=[0]*(temp+1)
for a,b in lst:
    lst2[a]=b
total = 0
temp2 = 0
for i in range(maxin+1):
    if lst2[i] > temp2:
        temp2 = lst2[i]
    total += temp2
temp2 = 0
for i in range(temp,maxin,-1):
    if lst2[i] > temp2:
        temp2 = lst2[i]
    total += temp2
print(total)