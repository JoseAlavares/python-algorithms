def partition(arr):
    pivot = arr[0]
    minor_list = []
    mayor_list = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            minor_list.append(arr[i])
        else:
            mayor_list.append(arr[i])

    return minor_list, pivot, mayor_list

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    
    minor, pivot, mayor = partition(arr)

    #return minor + [pivot] + mayor
    return quick_sort(minor) + [pivot] + quick_sort(mayor)

score = [8, 12, 3, 11, 5, 9, 10, 4, 15, 7]
#score = [2, 3, 1]
#print(quick_sort(score))