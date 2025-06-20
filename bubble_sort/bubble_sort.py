def main():
    my_array=[1,5,3]
    results = bubble_sort(my_array)
    print(results)
    
    #results=bubble_reverse(my_array)
    #print(results)
# def bubble_duplicate():
#    pass
# def bubble_reverse(my_array):
#     sorted_list=bubble_sort(my_array)
#     return sorted_list[::]
#     pass 
def bubble_sort(my_array):
    # TODO: Implement bubble sort
    # my_array=[1,2,3]
    n=len(my_array)
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if my_array[j]>my_array[j+1]:
                my_array[j],my_array[j+1]=my_array[j+1],my_array[j]
                swapped=True
        if not swapped:
                break
    print("Sorted array:", my_array)
    return my_array 
    
main()



