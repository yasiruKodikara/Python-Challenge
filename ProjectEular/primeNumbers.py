from math import sqrt

pf = []
for i in range(2,100):
    isPrime = True
    for j in range(2,int(round(sqrt(i),1))+1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        pf.append(i)
print(pf)