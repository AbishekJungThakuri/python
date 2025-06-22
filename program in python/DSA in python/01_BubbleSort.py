# Bubble sort in ascending order

def bubble_sort(data):
    
    # initialize a variable as False
    # to indicate that no swaps have taken place 
    swapped = False
    for i in range(len(data)-1):   # When the correct element is placed at the second position, the correct element will be placed at the first position as well.
        for j in range(len(data)-1-i):   
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                
                # if any element is swapped, 
                # set swapped to True.
                swapped = True
    
    
        # if swapped remains False after the inner loop,
        # it means none of the elements were swapped
        # therefore, the list is already sorted, and we can exit.
        if not swapped:
           break
    
    return data


data_list = [4, 6, 99, 45, 0]

sorted_list = bubble_sort(data_list)
print(sorted_list)


# Best Case Time Complexity	     O(n)
# Worst Case Time Complexity	 O(n2)
# Average Case Time Complexity   O(n2)
# Space Complexity	             O(1)
