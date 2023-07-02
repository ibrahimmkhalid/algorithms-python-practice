def fn(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
    return arr

print(fn([1,44,20,66,-10,99]))


