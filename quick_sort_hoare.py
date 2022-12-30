def partition(arr, minor, mayor):
    pivot = arr[minor]
    left = minor + 1
    rigth = mayor

    while True:
        while left <= rigth and arr[left] <= pivot:
            left += 1
        while left <= rigth and arr[rigth] >= pivot:
            rigth -= 1
        if rigth < left:
            break
        else:
            arr[left], arr[rigth] = arr[rigth], arr[left]
        
    arr[minor], arr[rigth] = arr[rigth], arr[minor]

    return rigth

def quick_sort_hoare(arr, minor, mayor):
    if minor < mayor:
        pivot = partition(arr, minor, mayor)
        quick_sort_hoare(arr, minor, pivot - 1)
        quick_sort_hoare(arr, pivot + 1, mayor)

score = [9, 1, 4, 9, 3, -1, 15, 12, 3, 9, -3, 7, 5, 2, 10]
quick_sort_hoare(score, 0, len(score) - 1)
print(score)