
def printarr(arr):
    for i in range (len(arr)):
        print(arr[i], end=" ")
    print("\n")

def partition(arr, floor, roof):
    pivot = arr[roof]
    i = floor - 1

    for j in range (floor, roof):
        if arr[j] <= pivot:
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            
    tmp = arr[i+1]
    arr[i+1] = arr[roof]
    arr[roof] = tmp

    printarr(arr[floor:roof])
    return i + 1
    

def quicksort(arr, floor, roof):
    if len(arr) == 1:
        return arr
    if floor < roof:
        q = partition(arr, floor, roof)
        quicksort(arr, floor, q - 1)
        quicksort(arr, q + 1, roof)

if __name__ == "__main__":
    # roof = int(input())
    # arr = list(map(int, input().rstrip().split()))
    
    roof = 7
    arr = [5, 8, 1, 3, 7, 9, 2]

    # print(arr)
    quicksort(arr, 0, roof - 1)
    print(arr)