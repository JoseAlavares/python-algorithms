#!/usr/bin/python

import math

def linear_search(arr, item):
    for _item in arr:
        if item == _item:
            return True
    
    return False

def jump_search(arr, item, low, high, jump_size):
    print(low, high)
    if low > len(arr) or high > len(arr):
        return False

    if item == arr[low] or item == arr[high]:
        return True
    elif item > arr[low] and item < arr[high]:
        return linear_search(arr[low:high], item)
    elif item > arr[low] and item > arr[high]:
        return jump_search(arr, item, high, high + jump_size, jump_size)

def main(arr, item):
    jump_size = int(math.floor(math.sqrt(len(arr))))
    
    return jump_search(arr, item, 0, jump_size, jump_size)

#print(main(sorted([9, 1, 4, -1, 15, 12, 3, -3, 7, 5, 2, 10, 100, 101, 222]), 100))
