def solution():
    n = list(input())
    zero = n.count('0') // 2
    one = n.count('1') // 2

    for _ in range(zero):
        n.pop(-(n[::-1].index('0')) - 1)

    for _ in range(one):
        n.pop(n.index('1'))

    print(''.join(n))


solution()