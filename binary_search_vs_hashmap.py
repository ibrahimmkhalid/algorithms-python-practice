import pandas as pd

data = pd.read_csv("./datas/MOCK_DATA.csv")["first_name"].tolist()

import random

find_name = data[random.randint(0, len(data))]

print("Naive search")
for i, d in enumerate(data):
    if d == find_name:
        print(d)
        print(f"Found after {i} comparisons")
        break


def naive_search(name) -> int:
    for i, d in enumerate(data):
        if d == name:
            print(d)
            print(f"Found after {i} comparisons")
            return i
    return -1


print("---")
print()

print("Hashmap")
hashmap = [None] * 26


def hashkey(item: str) -> int:
    return ord(item.upper()[0]) - 65


for d in data:
    idx = hashkey(d)
    if hashmap[idx] is None:
        hashmap[idx] = [d]
    else:
        assert type(hashmap[idx]) == list
        hashmap[idx].append(d)


def hashmap_search(hashmap, item) -> int:
    i = 0
    for d in hashmap[hashkey(item)]:
        if d == item:
            print(d)
            print(f"Found after {i} comparisons")
            return i
        i += 1
    return -1


hashmap_search(hashmap, find_name)

print("---")
print()

print("Binary search")
import math


def binary_search(arr, x) -> int:
    i = 0
    lo = 0
    hi = len(arr)
    while hi > lo:
        mid = math.floor((hi + lo) / 2)
        if arr[mid] == x:
            print(arr[mid])
            print(f"Found after {i} comparisons")
            return i
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
        i = i + 1
    return -1


import numpy as np

sorted_data = np.sort(data)
binary_search(sorted_data, find_name)

navg = bavg = havg = 0
for name in data:
    navg += naive_search(name)
    bavg += binary_search(sorted_data, name)
    havg += hashmap_search(hashmap, name)

print("Average time for naive search", navg / len(data))
print("Average time for hashmap search", havg / len(data))
print("Average time for binary search", bavg / len(data))
print("Thoug binary search is faster, it only works if the data is sorted already")
