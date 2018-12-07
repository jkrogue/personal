def bubble_sort(arr):
    swapped = True
    last_swapped = len(arr) - 1
    while swapped:
        swapped = False
        for i in range(last_swapped):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
                last_swapped = i


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []

    i, j = 0, 0

    while len(result) < len(left) + len(right):

        if i >= len(left):
            result.extend(right[j:])
        elif j >= len(right):
            result.extend(left[i:])
        elif left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result

import random

def quicksort(arr):
    quicksort_recur(arr, 0, len(arr) - 1)

def quicksort_recur(arr, start, end):
    if start < end:
        pivot = random.randint(start,end)

        arr[pivot], arr[end] = arr[end], arr[pivot]

        split = partition(arr, start, end)

        quicksort_recur(arr, start, split-1)
        quicksort_recur(arr, split+1, end)

def partition(arr, start, end):
    done = False
    left, right = start, end
    while not done:
        while left < right and arr[left] <= arr[end]:
            left += 1
        while right > left and arr[right] >= arr[end]:
            right -= 1
        if left >= right:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[left], arr[end] = arr[end], arr[left]

    return left

if __name__ == '__main__':
    import numpy as np
    import datetime

    for n in range(1000, 2001, 1000):
        print('{} items'.format(n))
        print('Bubble sort')
        np.random.seed(1)
        my_list = np.random.randint(0,n,size=(n))
        print(my_list[:25])
        start = datetime.datetime.now()
        bubble_sort(my_list)
        bubble_sort_runtime = datetime.datetime.now() - start
        print(my_list[:25])

        print('\nMerge sort')
        np.random.seed(1)
        my_list = np.random.randint(0,n,size=(n))
        print(my_list[:25])
        start = datetime.datetime.now()
        my_list = merge_sort(my_list)
        merge_sort_runtime = datetime.datetime.now() - start
        print(my_list[:25])

        print('\nQuick sort')
        np.random.seed(1)
        my_list = np.random.randint(0,n,size=(n))
        print(my_list[:25])
        start = datetime.datetime.now()
        quicksort(my_list)
        quick_sort_runtime = datetime.datetime.now() - start
        print(my_list[:25])

        print("\nRuntimes with {} items: \nBubble sort: {}\nMerge sort: {}\nQuick sort: {}\n"
            .format(n,bubble_sort_runtime,merge_sort_runtime,quick_sort_runtime))


