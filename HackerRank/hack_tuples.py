N = int(input())
inputs = [int(x) for x in input().split(" ")]
tup = tuple(inputs)

print(hash(tup))