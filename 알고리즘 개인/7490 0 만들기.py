def solution(i,result):
    if i==(N-1):
        result=result+str(lst[i])
        if eval(result.replace(' ',''))==0:
            print(result)
        return
    solution(i + 1, result + str(lst[i]) + ' ')
    solution(i + 1, result + str(lst[i]) + '+')
    solution(i+1,result+str(lst[i])+'-')

TC=int(input())
for _ in range(TC):
    N=int(input())
    lst=list(range(1,N+1))
    solution(0,"")
    print()