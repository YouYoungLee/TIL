import sys
input = sys.stdin.readline

N,G=input().split()
tmp=[]
for _ in range(int(N)):
    tmp.append(input())
people=list(set(tmp))
if G=='Y':
    print(len(people))
elif G=='F':
    print(len(people)//2)
else:
    print(len(people)//3)
