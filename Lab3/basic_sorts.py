# Bubble Sort, Selection Sort, and Insertion Sort (all return a new sorted list)

def bubble_sort(arr, show_steps=False):
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if show_steps:
            print(f"Pass {i + 1}: {a}")
        if not swapped:
            break
    return a

def selection_sort(arr, show_steps=False):
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        if show_steps:
            print(f"Step {i + 1}: {a}")
    return a

def insertion_sort(arr, show_steps=False):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        if show_steps:
            print(f"Step {i}: {a}")
    return a

if __name__ == "__main__":
    sample = [64, 25, 12, 22, 11]
    print("Original array:", sample)

    print("\n--- Bubble Sort ---")
    print("Result:", bubble_sort(sample, show_steps=True))

    print("\n--- Selection Sort ---")
    print("Result:", selection_sort(sample, show_steps=True))

    print("\n--- Insertion Sort ---")
    print("Result:", insertion_sort(sample, show_steps=True))