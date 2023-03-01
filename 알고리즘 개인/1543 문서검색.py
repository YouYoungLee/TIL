lst=input()
senten=input()
answer=0
index=0
for i in range(len(lst)):
    if index > i:
        continue
    if senten==lst[i:i+len(senten)]:
        answer+=1
        index = i+len(senten)

print(answer)