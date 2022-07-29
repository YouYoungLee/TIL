a,b,c,d=map(int,input().split())
e=(a*b*c*d/8/1024/1024)
e=round(e,1)
print(f'{e} MB')
