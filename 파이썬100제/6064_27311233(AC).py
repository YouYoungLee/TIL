a,b,c=map(int,input().split())
print((b if a>b else a) if ((b if a>b else a)<c) else c)
