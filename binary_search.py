from quick_sort import quick_sort
import math

def binary_search(arr, search, min, max):    
    if min > max:
        return False

    middle = (min + max) // 2 
    middleItem = arr[middle]   
    
    if search == middleItem:
        return True    
    elif search > middleItem:
        return binary_search(arr, search, middle + 1, max)
    elif search < middleItem:        
        return binary_search(arr , search, min, middle - 1)

score = quick_sort([9, 1, 4, -1, 15, 12, 3, -3, 7, 5, 2, 10])
print(binary_search(score, 100, 0, len(score) - 1))
