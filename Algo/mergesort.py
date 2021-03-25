
def mergeSort(arr):
    # global inv
    if len(arr) > 1:
 
        L, R = arr[:len(arr)//2], arr[len(arr)//2:]
        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                # inv += 1
                arr[k] = L[i]
                i += 1
            else:
                # inv += 1
                arr[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 

def countInnv(arr):
    inv = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv

if __name__ == '__main__':
    # global inv
    # inv = 0
    arr = [9492052, 241944, 5743396, 5758608, 6053545]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
    inv = countInnv(arr)
    print(f"Inversions {inv}")