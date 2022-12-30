#!/usr/bin/python

#bubble_sort algorithm
def bubble_sort(array):
    counter = 0
    comparations = 0
    changes = True
    length = len(array) - 1

    while changes:
        changes = False

        for j in range(0, length - counter):
            comparations += 1
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

                changes = True

        counter += 1
    return array, comparations

numbers = [1000, 40, 20, 29, 10, 12, 102, 2389, 35, 89]
arr, comp = bubble_sort(numbers)
print(arr)
print(comp)