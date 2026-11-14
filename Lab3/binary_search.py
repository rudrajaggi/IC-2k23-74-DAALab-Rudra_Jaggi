# Iterative Binary Search returning target index or -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    sorted_nums = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
    print("Sorted array:", sorted_nums)

    t1 = 23
    print(f"Search {t1} -> Index: {binary_search(sorted_nums, t1)}")

    t2 = 50
    print(f"Search {t2} -> Index: {binary_search(sorted_nums, t2)}")