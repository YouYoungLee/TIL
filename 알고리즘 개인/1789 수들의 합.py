S=int(input())
i=1
tmp=0
while True:
    tmp+=i
    if(tmp>S):
        print(i-1)
        break
    i+=1