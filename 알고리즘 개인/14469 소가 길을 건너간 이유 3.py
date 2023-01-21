N=int(input())
lst=[list(map(int,input().split())) for _ in range(N)]
lst.sort(key=lambda x: x[0])
time=0
for i in range(N):
    if time<lst[i][0]:
        time=lst[i][0]+lst[i][1]
    else:
        time+=lst[i][1]
print(time)


