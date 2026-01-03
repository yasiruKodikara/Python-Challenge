def bubbleSort(arr):
    n = len(arr)
    for k in range(0,n):
        for j in range(0,n-k-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


arr = [31415926535897932384626433832795, 1, 3, 10, 3, 5]

print('before sorting ',arr)

bubbleSort(arr)

print('after sorting ',arr)