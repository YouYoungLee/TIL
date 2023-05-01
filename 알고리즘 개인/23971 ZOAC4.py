h,w,n,m=map(int,input().split())
tmpn=1+n
tmpm=1+m
tmph=0
tmpw=0
while True:
    if h<=0:
        break
    h-=tmpn
    tmph+=1
while True:
    if w<=0:
        break
    w-=tmpm
    tmpw+=1
print(tmph*tmpw)