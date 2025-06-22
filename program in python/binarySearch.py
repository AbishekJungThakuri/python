inputNum = input("Enter number: ")
num = inputNum.split()
arr = [int(n) for n in num]


def BinarySearch(arr,start,end,search):
    
    if start <= end:
        mid = (start+end)//2

        if arr[mid] == search:
            return mid
        elif arr[mid] > search:
            return BinarySearch(arr,start,mid-1,search)
        else:
            return BinarySearch(arr, mid+1, end, search)
    
    else:
        return -1   # Element is not present in the array

   
    
searchElement = int(input("Enter the elements to search: "))
result = BinarySearch(arr, 0 ,len(arr)-1, searchElement)

if result == -1:
    print("Element is not present in array")
else:
     print("Element is present at index", str(result))
