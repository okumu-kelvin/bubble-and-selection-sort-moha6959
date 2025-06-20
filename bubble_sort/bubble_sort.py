def main():
    my_array=[1,5,3]
    results = bubble_sort(my_array)
    print(results)
    
    
def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    # my_array=[1,2,3]
    n=len(unsorted_list)
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if unsorted_list[j]>unsorted_list[j+1]:
                unsorted_list[j],unsorted_list[j+1]=unsorted_list[j+1],unsorted_list[j]
                swapped=True
        if not swapped:
                break
    print("Sorted array:", unsorted_list)
    return unsorted_list 
    
main()



