n = int(input())
l = list()
total = 0
for i in range(n):
    t = int(input())
    l.append(t)

for number in l:
    total += number
total1=str(total)
total2=list(total1)

final = total2[:10]
print(''.join(final))




