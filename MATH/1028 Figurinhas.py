def mdc(n1, n2):
    if n1 > n2:
        while n2:
            n1, n2 = n2, n1 % n2
        return n1
    else:
        while n1:
            n2, n1 = n1, n2 % n1
        return n2

# PROGRAMA PRINCIPAL

n = int(input())

for _ in range(n):
    f1, f2 = map(int, input().split())
    print(mdc(f1, f2))
