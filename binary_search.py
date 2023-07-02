import math
def fn(arr, x):
    lo = 0
    hi = len(arr)
    while hi > lo:
        mid = math.floor((hi + lo)/2)
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return False

print(fn([1,4,16,29,36,39,40,44,57,66,99], 99))
print(fn([1,4,16,29,36,39,40,44,57,66,99], 1))
print(fn([1,4,16,29,36,39,40,44,57,66,99], 36))
print(fn([1,4,16,29,36,39,40,44,57,66,99], 33))
print(fn([1,4,16,29,36,39,40,44,57,66,99], 1000))
print(fn([1,4,16,29,36,39,40,44,57,66,99], -10))

