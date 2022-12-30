#!/usr/bin/python

def binary_search(arr, item, min, max):    
    if min > max:
        return False

    middle = (min + max) // 2
    
    if arr[middle] == item:
        return True
    elif arr[middle] > item:
        return binary_search(arr, item, min, middle -1)
    elif arr[middle] < item:
        return binary_search(arr, item, middle + 1, max)

arr = [1, 3, 2, 45, 7, 39, 10]
arr = sorted(arr)
length = len(arr) - 1
result = binary_search(arr, -1, 0, length)
print(result)