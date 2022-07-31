a,b,c=map(int,input().split())
d= 1
while True:
    if d%a==0 and d%b==0 and d%c==0:
        break
    else:
        d+=1
print(d)
