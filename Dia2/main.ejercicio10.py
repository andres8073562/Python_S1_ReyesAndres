
####//


def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (arr[j] > arr[j + 1]) == ascending:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n - 1):
        extreme_idx = i
        for j in range(i + 1, n):
            if (arr[j] < arr[extreme_idx]) == ascending:
                extreme_idx = j
        arr[i], arr[extreme_idx] = arr[extreme_idx], arr[i]
    return arr

def insertion_sort(arr, ascending=True):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and (arr[j] > key) == ascending:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


arr = [64, 25, 12, 22, 11]
print("Ordenación por burbuja ascendente:", bubble_sort(arr.copy(), ascending=True))
print("Ordenación por burbuja descendente:", bubble_sort(arr.copy(), ascending=False))
print("Ordenación por selección ascendente:", selection_sort(arr.copy(), ascending=True))
print("Ordenación por selección descendente:", selection_sort(arr.copy(), ascending=False))
print("Ordenación por inserción ascendente:", insertion_sort(arr.copy(), ascending=True))
print("Ordenación por inserción descendente:", insertion_sort(arr.copy(), ascending=False))


###/// Desarollado por Andres Reyes T.i 1097100508