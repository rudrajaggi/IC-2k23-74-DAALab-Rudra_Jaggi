# Student Record Manager supporting multi-field sorting, binary search, and timing comparison

import time

def sort_records(records, key_index, algo_choice):
    a = records.copy()
    n = len(a)

    if algo_choice == "1":  # Bubble Sort
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if a[j][key_index] > a[j + 1][key_index]:
                    a[j], a[j + 1] = a[j + 1], a[j]
    elif algo_choice == "2":  # Selection Sort
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if a[j][key_index] < a[min_idx][key_index]:
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
    elif algo_choice == "3":  # Insertion Sort
        for i in range(1, n):
            curr = a[i]
            j = i - 1
            while j >= 0 and a[j][key_index] > curr[key_index]:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = curr
    elif algo_choice == "4":  # Merge Sort
        if n <= 1:
            return a
        mid = n // 2
        left = sort_records(a[:mid], key_index, "4")
        right = sort_records(a[mid:], key_index, "4")
        a = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][key_index] <= right[j][key_index]:
                a.append(left[i])
                i += 1
            else:
                a.append(right[j])
                j += 1
        a.extend(left[i:])
        a.extend(right[j:])
    elif algo_choice == "5":  # Quick Sort (last element pivot)
        if n <= 1:
            return a
        pivot = a[-1][key_index]
        less = [x for x in a[:-1] if x[key_index] <= pivot]
        greater = [x for x in a[:-1] if x[key_index] > pivot]
        a = sort_records(less, key_index, "5") + [a[-1]] + sort_records(greater, key_index, "5")
    elif algo_choice == "6":  # Heap Sort
        def heapify(arr, size, root):
            largest = root
            l, r = 2 * root + 1, 2 * root + 2
            if l < size and arr[l][key_index] > arr[largest][key_index]:
                largest = l
            if r < size and arr[r][key_index] > arr[largest][key_index]:
                largest = r
            if largest != root:
                arr[root], arr[largest] = arr[largest], arr[root]
                heapify(arr, size, largest)

        for i in range(n // 2 - 1, -1, -1):
            heapify(a, n, i)
        for i in range(n - 1, 0, -1):
            a[0], a[i] = a[i], a[0]
            heapify(a, i, 0)
    return a

def binary_search_roll(records, target_roll):
    low, high = 0, len(records) - 1
    while low <= high:
        mid = (low + high) // 2
        if records[mid][0] == target_roll:
            return records[mid]
        elif records[mid][0] < target_roll:
            low = mid + 1
        else:
            high = mid - 1
    return None

def display_records(records):
    print(f"\n{'Roll No':<10} | {'Name':<15} | {'Marks':<6}")
    print("-" * 36)
    for r in records:
        print(f"{r[0]:<10} | {r[1]:<15} | {r[2]:<6}")

def main():
    # Tuple format: (roll_no, name, marks)
    students = [
        (105, "Aarav", 84),
        (101, "Riya", 92),
        (108, "Kabir", 76),
        (103, "Meera", 88),
        (102, "Vikram", 69),
        (107, "Ananya", 95),
        (104, "Rohan", 81),
        (106, "Sneha", 90)
    ]
    sorted_by_roll = False

    while True:
        print("\n1. View Records  2. Sort Records  3. Search by Roll (Binary Search)  4. Benchmark All Sorts  5. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            display_records(students)
        elif choice == "2":
            print("Sort by: 0=Roll No, 1=Name, 2=Marks")
            field = int(input("Field: "))
            print("Algorithm: 1=Bubble, 2=Selection, 3=Insertion, 4=Merge, 5=Quick, 6=Heap")
            algo = input("Algorithm: ").strip()
            students = sort_records(students, field, algo)
            sorted_by_roll = (field == 0)
            display_records(students)
        elif choice == "3":
            if not sorted_by_roll:
                print("Sorting records by Roll No first...")
                students = sort_records(students, 0, "4")
                sorted_by_roll = True
            roll = int(input("Enter Roll No to search: "))
            res = binary_search_roll(students, roll)
            if res:
                print(f"Found -> Roll: {res[0]}, Name: {res[1]}, Marks: {res[2]}")
            else:
                print("Student not found.")
        elif choice == "4":
            names = [("1", "Bubble"), ("2", "Selection"), ("3", "Insertion"), ("4", "Merge"), ("5", "Quick"), ("6", "Heap")]
            times = []
            for code, label in names:
                t0 = time.perf_counter()
                for _ in range(500):  # Repeat 500x so small dataset timing is measurable
                    sort_records(students, 2, code)
                dt = (time.perf_counter() - t0) * 1000
                times.append((dt, label))
            times.sort()
            print("\n--- Performance Report (500 runs on dataset) ---")
            for dt, label in times:
                print(f"{label:<12}: {dt:.4f} ms")
            fastest_t, fastest_name = times[0]
            slowest_t, slowest_name = times[-1]
            print(f"Fastest: {fastest_name} ({fastest_t:.4f} ms)")
            print(f"Slowest: {slowest_name} ({slowest_t:.4f} ms)")
            print(f"{fastest_name} was {slowest_t / fastest_t:.2f}x faster than {slowest_name}.")
        elif choice == "5":
            break

if __name__ == "__main__":
    main()