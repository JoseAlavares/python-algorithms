#My poor code :(
def sort_selection(arr):
    actual = None
    length = len(arr) - 1
    
    for i in range(0, length):            
        actual = arr[i]        
        p_minor = None

        for j in range(i + 1, length + 1):
            if actual > arr[j]:
                actual = arr[j]
                p_minor = j
                
        if p_minor != None:
            temp = arr[i]
            arr[i] = arr[p_minor]
            arr[p_minor] = temp

            

    return arr

score = [5, 7, 3, 1, 4, 2, 6]
print(sort_selection(score))

#The code of the tutorial
def sort_selection_2(arr):
    length = len(arr)

    for i in range(length - 1):
        menor = i

        for j in range(i + 1, length):
            if arr[j] < arr[menor]:
                menor = j

        temp = arr[menor]
        arr[menor] = arr[i]
        arr[i] = temp

    return arr

score = [5, 7, 3, 1, 4, 2, 6]
print(sort_selection_2(score))