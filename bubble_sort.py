#!/usr/bin/python

#bubble_sort algorithm
def bubble_sort(array):
    length = len(array) - 1

    for i in range(0, length):
        for j in range(0, length):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array

numbers = [1000, 40, 20, 29, 10, 12, 102, 2389, 35, 89]
result = bubble_sort(numbers)
print(result)



