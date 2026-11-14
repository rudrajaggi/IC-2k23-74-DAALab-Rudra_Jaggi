# Lab 3: Sorting, Searching, Hashing, and Empirical Analysis

## Section C, D & E Programs

### 1. Basic Sorting Algorithms (`basic_sorts.py`)
* **Aim:** Implement Bubble Sort, Selection Sort, and Insertion Sort as standalone functions returning new sorted lists while printing intermediate steps.
* **Logic:** Each function copies the input list to avoid mutating the original. Bubble sort swaps adjacent out-of-order elements per pass, selection sort selects the minimum element per pass, and insertion sort shifts larger elements right to insert each item.
* **Sample Input / Output:**
  ```text
  Original array: [64, 25, 12, 22, 11]
  --- Bubble Sort ---
  Pass 1: [25, 12, 22, 11, 64]
  Pass 2: [12, 22, 11, 25, 64]
  Pass 3: [12, 11, 22, 25, 64]
  Pass 4: [11, 12, 22, 25, 64]
  Result: [11, 12, 22, 25, 64]