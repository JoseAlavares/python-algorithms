#5, 7, 1, 3, 4, 2, 6
#for i in range(10, -1, -1):
    #print(i)

#My poor code :(
def sort_insertion(arr):
    length = len(arr)

    for i in range(length-1):
        actual = i + 1
        for j in range(actual, -1, -1):            
            if arr[actual] < arr[j]:
                temp = arr[j]
                arr[j] = arr[actual]
                arr[actual] = temp
                actual = j

    return arr

score = [5, 7, 1, 3, 8, 4, 9, 2, 6]
print(sort_insertion(score))

#Code of the tutorial
def sort_insertion_2(arr):
    length = len(arr)
    
    for i in range(length):
        actual = arr[i]
        index = i

        while index > 0 and arr[index - 1] > actual:
            arr[index] = arr[index - 1]
            index -=  1

        arr[index] = actual

    return arr

score = [5, 7, 1, 3, 8, 4, 9, 2, 6]
print(sort_insertion_2(score))
