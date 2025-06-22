
inputNum = input('Enter a numbers: ')
num = inputNum.split()
arr = [int(n) for n in num]

def maxmin(start,end,arr,max,min):
    if(start == end):
        max = min = arr[start];