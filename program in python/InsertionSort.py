
inputNum = input('Enter a numbers: ')
num = inputNum.split()
arr = [int(n) for n in num]

# Another method
# arr=[]
# for n1 in num:
#     n = int(n1)
#     arr.append(n)

def insertion(arr):
    n = len(arr)

    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = temp 

insertion(arr)
print("The sorted order numbers are:",arr)