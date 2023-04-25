S=input()
lst=[]
for i in range(len(S)):
    lst.append(S[i:])
lst.sort()
for i in lst:
    print(i)