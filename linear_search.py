#!/usr/bin/python

def linear_search(arr, item_search):
    for item in arr:
        if item == item_search:
            return True

    return False

array = [10, 30, 44, 398, 27, 67, 278, 6]
result = linear_search(array, 6)
print(result)