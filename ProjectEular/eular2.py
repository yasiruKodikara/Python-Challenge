def fibonacci():
    _sum = 0
    x = [0,1]
    while True:
        nt = x[-1] + x[-2]
        x.append(nt)
        if nt%2==0:
            _sum+=nt

        if nt>=4000000:
            break
    return x,_sum

n = int(input("Enter end number: "))
print(fibonacci())