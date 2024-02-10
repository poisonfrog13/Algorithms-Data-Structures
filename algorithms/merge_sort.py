import math 


def merge(array, start, mid, stop):

    stop += 1
    lst_1 = array[start:mid+1] + [math.inf]
    lst_2 = array[mid+1:stop] + [math.inf]
   
    x, y = 0, 0

    for i in range(start, stop):
        if lst_1[x] <= lst_2[y]:
            array[i] = lst_1[x]
            x += 1
        else:
            array[i] = lst_2[y]
            y += 1
    return array

def _merge_sort(array, start, stop):
    if start < stop:
        mid = math.floor((start + stop) / 2)
        _merge_sort(array, start, mid)
        _merge_sort(array, (mid+1), stop)
        merge(array, start, mid, stop)

def merge_sort(array):
    start = 0
    stop = len(array) - 1
    _merge_sort(array, start, stop)
    return array

