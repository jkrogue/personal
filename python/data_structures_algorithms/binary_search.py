def binary_search(array, value):
    left = 0
    right = len(array) - 1
    iter = 0
    while left <= right:
        iter += 1
        mid = (left + right) // 2
        if array[mid] == value:
            return mid, iter
        elif array[mid] < value:
            # go right
            left = mid + 1
        elif array[mid] > value:
            # go left
            right = mid - 1

    return -1, iter

def binary_search_recursive(array, value, left, right):
    mid = (left + right) // 2
    if left > right:
        return -1
    elif array[mid] == value:
        return mid
    elif array[mid] < value:
        # go right
        return binary_search_recursive(array, mid + 1, right)
    elif array[mid] > value:
        # go left
        return binary_search_recursive(array, left, mid - 1)

if __name__ == '__main__':
    my_list = list(range(1,9))

    # verifying it works
    print(my_list)
    idx, iter = binary_search(my_list,4)
    print('Searching for "4": index ',idx)

    # verifying recursive search
    print(my_list)
    idx = binary_search_recursive(my_list,4, 0, len(my_list) - 1)
    print('Searching for "4": index ',idx)

    # calcuating worst case
    my_list = list(range(8))
    idx, iter = binary_search(my_list,11)
    print('Number of iterations to search array length {}: {}'.format(len(my_list),iter))

    my_list = list(range(16))
    idx, iter = binary_search(my_list,17)
    print('Number of iterations to search array length {}: {}'.format(len(my_list),iter))

    my_list = list(range(32))
    idx, iter = binary_search(my_list,33)
    print('Number of iterations to search array length {}: {}'.format(len(my_list),iter))

    my_list = list(range(64))
    idx, iter = binary_search(my_list,101)
    print('Searching for "101"',idx)
    print('Number of iterations to search array length {}: {}'.format(len(my_list),iter))


    my_list = list(range(128))
    idx, iter = binary_search(my_list,129)
    print('Searching for "101"',idx)
    print('Number of iterations to search array length {}: {}'.format(len(my_list),iter))
