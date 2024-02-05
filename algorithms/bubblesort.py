def bubblesort(array: list) -> list:
    for x in range(0, len(array)-1):
        number = array[x]
        for y in range (1, len(array)):
            if array[y-1] > array[y]:
                number = array[y]
                array[y] = array[y-1]
                array[y-1] = number
    return array 


def bubblesort_2(array: list) -> list:
    for i in range(0, len(array)-1):
        for j in range(0, len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array