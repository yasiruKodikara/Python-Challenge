def fibonacci(n):
    x = [0,1]
    for i in range(n):
        nt = x[-1] + x[-2]
        x.append(nt)
    return x

n = int(input("Enter end number: "))
print(fibonacci(n))