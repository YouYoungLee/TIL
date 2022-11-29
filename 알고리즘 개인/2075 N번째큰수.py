import heapq
N=int(input())
q=[]
for _ in range(N):
    temp=list(map(int,input().split()))
    q.extend(temp)
    heapq.heapify(q)
    while(len(q)>N):
        heapq.heappop(q)
print(heapq.heappop(q))