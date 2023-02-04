def gcd(a,b):
    while b > 0:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b // gcd(a,b)


N1,N2 = map(int,input().split())


print(gcd(N1,N2))
print(lcm(N1,N2))