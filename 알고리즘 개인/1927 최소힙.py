import heapq
import sys

input = sys.stdin.readline

N=int(input())
q=[]
for _ in range(N):
    temp=int(input())
    if temp==0:
        if len(q)==0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q,temp)

