# Selection sort works by repeatedly selecting the smallest (or largest) unsorted element and placing it towards the beginning of the list.

# Ascending order
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i

        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[min_index],lst[i] = lst[i],lst[min_index]
    
    return lst

data = [6, 4, 1, 9, 17, 11]
sorted_data = selection_sort(data)
print(sorted_data)

# Time complexity   O(n2)
# Space complexity  O(1)