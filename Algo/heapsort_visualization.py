import math

def heapsort(arr):
    build_max_heap(arr)
    n = len(arr)
    for i in range (n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        n = n - 1 
        heapify(arr, n, 0)


def build_max_heap(arr):
    n = len(arr)
    for i in range (n // 2 - 1 , -1, -1):
        heapify(arr, n, i)


def heapify(arr, n, i):
    l = 2*i
    r = 2*i + 1
    maxi = i
    
    
    if l < n and arr[l] > arr[i]:
        maxi = l

    if r < n and arr[r] > arr[maxi]:
        maxi = r

    if maxi != i:
        arr[i], arr[maxi] = arr[maxi], arr[i]
        print(arr)
        heapify(arr, n, maxi)


if __name__ == '__main__':
    arr0 = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    arr1 = [1,3,1,2,7,9,1,6,1,0,4,2]
    arr2 = [15,3,99,1,25,7,9,9,1,100,6,1,0,12,4,2,9,0,87,122,54]
    arr3 = [0,12,4,2,9,0,87,122,54,1,2,11,55,99]

    print(arr0)
    heapsort(arr0)
    print(arr0)