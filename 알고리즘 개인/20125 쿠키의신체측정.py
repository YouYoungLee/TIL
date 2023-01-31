N=int(input())
lst=[]
sign=False
for _ in range(N):
    lst.append(input())
for i in range(N):
    for j in range(N):
        if lst[i][j]=='*':
            x=i+2
            y=j+1
            print(x,y)
            sign=True
            break
    if sign:
        break
left_arm=0
for i in range(y-1):
    if lst[x-1][i]=='*':
        left_arm+=1
right_arm=0
for i in range(y,N):
    if lst[x-1][i]=='*':
        right_arm+=1
back = 0
line=0
for i in range(x,N):
    if lst[i][y-1]=="*":
        back+=1
        line=i
left_leg=0
for i in range(N-1,line,-1):
    if lst[i][y-2]=="*":
        left_leg+=1
right_leg=0
for i in range(N-1,line,-1):
    if lst[i][y]=='*':
        right_leg+=1
print(left_arm,right_arm,back,left_leg,right_leg)
