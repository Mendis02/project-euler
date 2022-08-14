# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    n = int(input())
    power = str(2 ** n)
    l = list(power)
    l1 = [eval(i) for i in l]
    total = sum(l1)
    print(total)