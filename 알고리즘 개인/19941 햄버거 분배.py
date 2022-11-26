import sys
input = sys.stdin.readline

N,K = map(int,input().split())
lst=list(input())
count=0

for i in range(N):
    if lst[i]=='P':
        for ni in range(i-K,i+K+1):
            if 0<=ni<N and lst[ni]=='H':
                    lst[ni]='E'
                    count+=1
                    break

print(count)