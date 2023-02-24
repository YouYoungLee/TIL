import copy

S=input()
S=list(S)
S2=S.copy()

# 1일 때
tmpa=0
tmpb=0
for i in range(len(S)):
    if S[i]=='1':
        S[i]='0'
        nx=0
        while True:
            nx+=1
            if nx+i<len(S) and S[i+nx]=='1':
                S[i+nx]='0'
            else:
                break
        tmpa+=1
# 0일 때
for i in range(len(S2)):
    if S2[i] == '0':
        S2[i] = '1'
        nx = 0
        while True:
            nx += 1
            if nx + i < len(S2) and S2[i + nx] == '0':
                S2[i + nx] = '1'
            else:
                break
        tmpb += 1
print(min(tmpa,tmpb))


