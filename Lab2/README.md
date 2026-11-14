# Lab 2: Arrays, Matrices, and Sparse Representation

## 1. 1D Array Operations (`array_1d_operations.py`)
* **Aim:** Perform insertion, deletion, linear search, and left/right rotations on a 1D Python list with bounds validation.
* **Logic:** Uses list indexing and slicing (`arr[k:] + arr[:k]`) after taking `k % len(arr)` to handle rotations cleanly. Checks `0 <= index <= len(arr)` before modifying the list so invalid indices do not crash the program.
* **Sample Input / Output:**
  ```text
  Enter initial array elements separated by space: 10 20 30 40 50
  Current array: [10, 20, 30, 40, 50]
  Choose an option: 1
  Enter index to insert at: 2
  Enter value to insert: 25
  Array: [10, 20, 25, 30, 40, 50]
  Choose an option: 1
  Enter index to insert at: 10
  Enter value to insert: 99
  Error: Index out of range.
  Array: [10, 20, 25, 30, 40, 50]