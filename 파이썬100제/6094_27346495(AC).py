n = int(input())      #개수를 입력받아 n에 정수로 저장
a = input().split()  #공백을 기준으로 잘라 a에 순서대로 저장
for i in range(n) :  #0부터 n-1까지...
  a[i] = int(a[i])       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장
small=0
for i in range(len(a)):
    if i==0:
        small=a[i]
    else:
        if a[i]<small:
            small=a[i]
print(small)
