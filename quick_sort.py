import math
arr = [24, 48, 26, 2, 16, 32, 31, 25, 50, 19]

def qsort(arr, lo, hi):
    if lo < hi:
        pivotIdx = partition(arr, lo, hi)
        if pivotIdx >= 1:
            qsort(arr, lo, pivotIdx)
        qsort(arr, pivotIdx + 1, hi)
pass

def partition(arr, lo, hi):
    pivotIdx = (hi + lo) // 2
    pivot = arr[pivotIdx]

    left = lo
    right = hi

    while True:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left >= right:
            break

        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return right
pass


print(arr)
qsort(arr, 0, len(arr) - 1)
print(arr)
