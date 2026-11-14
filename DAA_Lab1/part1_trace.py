# Program to find the maximum element and sort a list step by step

arr = [8, 3, 15, 6, 2]
print("Original list:", arr)

# Finding largest element
max_val = arr[0]
comparisons = 0
for i in range(1, len(arr)):
    comparisons += 1
    if arr[i] > max_val:
        max_val = arr[i]
    print(f"i={i}, A[i]={arr[i]}, max={max_val}, comparisons={comparisons}")

print("Largest number:", max_val)
print("Total comparisons:", comparisons)

# Selection sort to sort from smallest to largest
sorted_arr = arr.copy()
n = len(sorted_arr)
print("\nSorting steps (Selection Sort):")
for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if sorted_arr[j] < sorted_arr[min_idx]:
            min_idx = j
    sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    print(f"Step {i+1}: {sorted_arr}")

print("Sorted list:", sorted_arr)