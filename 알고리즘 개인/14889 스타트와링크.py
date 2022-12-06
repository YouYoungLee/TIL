from itertools import combinations
from itertools import permutations
import sys; input=sys.stdin.readline
n=int(input())
arr=[i for i in range(n)]
comb=list(combinations(arr,n//2))
players=[]
for i in range(n):
    players.append(list(map(int,input().split())))
ans=2000
for x in range(len(comb)//2): # 절반까지만 한다.
    start,link=0,0 # start,link의 값들을 저장할 변수
    for a,b in list(permutations(comb[x],2)): # permuatation을 이용해서 구해주도록 다 더해주도록한다.
        start+=players[a][b]
    for a,b in list(permutations(list(set(arr)-set(comb[x])),2)):
        link+=players[a][b]
    ans=min(abs(start-link),ans) # 절댓값 붙여줘서 최솟값을 구할 것
print(ans)