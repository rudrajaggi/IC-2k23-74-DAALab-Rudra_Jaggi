# Program to perform insert, delete, linear search, and rotations on a 1D array

def insert_element(arr, index, value):
    if index < 0 or index > len(arr):
        print("Error: Index out of range.")
        return arr
    arr.insert(index, value)
    return arr

def delete_element(arr, index):
    if len(arr) == 0:
        print("Error: Array is empty.")
        return arr
    if index < 0 or index >= len(arr):
        print("Error: Index out of range.")
        return arr
    removed = arr.pop(index)
    print(f"Deleted {removed} from index {index}.")
    return arr

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def rotate_left(arr, k):
    if len(arr) == 0:
        return arr
    k = k % len(arr)
    return arr[k:] + arr[:k]

def rotate_right(arr, k):
    if len(arr) == 0:
        return arr
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

def main():
    raw = input("Enter initial array elements separated by space: ").strip()
    arr = [int(x) for x in raw.split()] if raw else []
    print("Current array:", arr)

    while True:
        print("\n1. Insert  2. Delete  3. Linear Search  4. Rotate Left  5. Rotate Right  6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            idx = int(input("Enter index to insert at: "))
            val = int(input("Enter value to insert: "))
            arr = insert_element(arr, idx, val)
            print("Array:", arr)
        elif choice == "2":
            idx = int(input("Enter index to delete: "))
            arr = delete_element(arr, idx)
            print("Array:", arr)
        elif choice == "3":
            target = int(input("Enter value to search: "))
            pos = linear_search(arr, target)
            if pos != -1:
                print(f"Value {target} found at index {pos}.")
            else:
                print(f"Value {target} not found in array.")
            print("Array:", arr)
        elif choice == "4":
            k = int(input("Enter positions to rotate left: "))
            arr = rotate_left(arr, k)
            print("Array:", arr)
        elif choice == "5":
            k = int(input("Enter positions to rotate right: "))
            arr = rotate_right(arr, k)
            print("Array:", arr)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()