#!/usr/bin/python

def higher(val1, val2):
    if val1 > val2:
        return val1
    
    return val2

def search_ones(arr):
    max_local = 0
    max_global = 0
    
    for i in range(len(arr)):
        print(i)
        if arr[i] == 1:
            max_local += 1
            max_global = higher(max_local, max_global)
            #max_global = max(max_local, max_global)
        else:
            max_local = 0
    
    return max_global        

print(search_ones([1, 0, 1, 1, 1, 0, 1, 1, 0,  1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))