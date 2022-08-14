t = int(input())
for a0 in range(t):
    fact = 1
    n = int(input())
    if n == 0:
        print(fact)
    else:
        for i in range(1,n+1):
            fact = fact*i
        fact1 = str(fact)
        l = list(fact1)
        l1 = [eval(i) for i in l]

        print(sum(l1))


