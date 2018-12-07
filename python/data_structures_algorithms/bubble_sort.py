def bubble_sort(arr, print_each = False):
    last_swap = len(arr) - 1
    iter = 0
    for i in range(len(arr)):
        swapped = False
        for j in range(last_swap):
            iter += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                last_swap = j
        if not swapped:
            break
        if print_each:
            print(arr)
    print(iter)

my_list = list(range(10,0,-1))
print(my_list)
bubble_sort(my_list)
print(my_list)
my_list = [21,4,1,3,9,20,25,6,21,14]
print(my_list)
bubble_sort(my_list)
print(my_list)
