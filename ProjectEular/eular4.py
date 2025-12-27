p = []
for i in range(100,1000):
    for j in range(1000,99,-1):
        m = i*j
        if str(m)[:] == str(m)[::-1]:
            p.append(m)
print(f'The largest palindromic number of three digits is : {max(p)}')