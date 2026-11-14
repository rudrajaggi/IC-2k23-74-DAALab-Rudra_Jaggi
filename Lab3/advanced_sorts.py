# Merge Sort, Quick Sort, and Heap Sort (all return a new sorted list)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Pivot strategy: Last element of the current subarray
def quick_sort(arr):
    a = arr.copy()
    _quick_sort_helper(a, 0, len(a) - 1)
    return a

def _quick_sort_helper(a, low, high):
    if low < high:
        p = _partition(a, low, high)
        _quick_sort_helper(a, low, p - 1)
        _quick_sort_helper(a, p + 1, high)

def _partition(a, low, high):
    pivot = a[high]  # Using last element as pivot
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

def heap_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        _heapify(a, i, 0)
    return a

def _heapify(a, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and a[left] > a[largest]:
        largest = left
    if right < n and a[right] > a[largest]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        _heapify(a, n, largest)

if __name__ == "__main__":
    sample = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", sample)
    print("Merge Sort:    ", merge_sort(sample))
    print("Quick Sort:    ", quick_sort(sample))
    print("Heap Sort:     ", heap_sort(sample))