def main():
    my_array = [3,2,1]

    # Ascending sort
    results = selection_sort(my_array)
    print( results)
def selection_sort(arr):
    # TODO: Implement selection sort
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
    pass
main()
