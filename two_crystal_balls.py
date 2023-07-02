import math
def fn(arr):
    n = len(arr)
    jump_length = math.floor(math.sqrt(n))
    last_jump = 0
    while last_jump < n and arr[last_jump] == False:
        last_jump = last_jump + jump_length
    
    if last_jump > n:
        return -1

    for i in range(last_jump - jump_length, last_jump):
        if arr[i] == True:
            return i
    return -1

def my_input(l, idx):
    arr = []
    for i in range (l):
        if i < idx:
            arr.append(False)
        else:
            arr.append(True)
    return arr

print(fn(my_input(100, 88)))
print(fn(my_input(10, 88)))
print(fn(my_input(1000000, 472)))
x = input("hello")
print(x)
