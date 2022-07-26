n=int(input())
if n<0 :
    if n%2==0 :
        print('A')      #주의 : 변수 A와 문자열 'A' / "A" 는 의미가 완전히 다르다. 
    else :
        print('B')
else :
    if n%2==0 :
        print('C')
    else :
        print('D')
