def insert_sort(array: list) -> list:
    for x in range(1, len(array)):
        number = array[x]
        y = x - 1
        while y >= 0 and array[y] > number:
            array[y+1] = array[y]
            y = y - 1
        array[y+1] = number
    return array

