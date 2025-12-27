c = 1
t = 0
while True:

    for i in range(1,21):
        if c%i==0:
            t+=1
    if t==20:
        print(c)
        break
    c += 1
    t = 0