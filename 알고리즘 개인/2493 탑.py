N=int(input())
lst = list(map(int,input().split()))

answer = [0]*N
stack = []
for i in range(len(lst)):
    while stack:
        if lst[stack[-1][0]]<lst[i]:
            stack.pop()
        else:
            answer[i]=stack[-1][0]+1
            break
    stack.append((i,lst[i]))
print(*answer)
