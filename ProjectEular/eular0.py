_sum = 0

for i in range(341000):
    sq = i**2
    if (sq)%2==1:
        _sum += sq
print(_sum)
