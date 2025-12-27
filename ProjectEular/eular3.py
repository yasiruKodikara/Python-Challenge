factors = []
primeFactors = []
c = 0
n = int(input("Enter the number:"))

for i in range(1,n+1):
    if n%i==0:
        factors.append(i)
print(factors)

for f in factors:
    c = 0
    for k in range(1,f+1):
        if f%k==0:
            c+=1

    if c==2:
        primeFactors.append(f)

print(primeFactors)
print(max(primeFactors))