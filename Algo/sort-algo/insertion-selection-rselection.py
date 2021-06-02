arr = [1,4,3,0,2,5,9,8,6,7]

print(arr)

def insertionSort(arr):
    for i in range (len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0) and (arr[j] > key):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr

def selectionSort(arr):
    for i in range (len(arr)):
        smallest = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = arr[j]
        tmp = arr[j]
        arr[j] = arr[smallest]
        arr[smallest] = tmp
    return arr

def recursiveSelectionSort(arr, n): 
    if n<=1: 
        return
    recursiveSelectionSort(arr, n -1)

    print(arr)
    
    last = arr[n-1] 
    j = n-2
    while (j>=0 and arr[j]>last): 
        arr[j+1] = arr[j] 
        j = j-1
    arr[j+1]=last 
    return arr

print(recursiveSelectionSort(arr, len(arr)))
# print(selectionSort(arr))
