
def _quicksort(array: list, low: int, high: int) -> None:
    if low < high:
        pivot = self._partition(array, low, high)
        self._quicksort(array, low, pivot)
        self._quicksort(array, pivot + 1, high)

def _partition(array: list, low: int, high: int) -> int:
    pivot = array[(high + low) // 2]
    i = low
    j = high

    while True:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]
    print(arr)

def sort(array: list) -> list:
    self._quicksort(array, 0, len(array) - 1)
    return array

arr = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
print(_partition(arr, 0, len(arr) - 1))