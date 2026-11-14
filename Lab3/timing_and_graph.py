# Empirical timing comparison of 6 sorting algorithms and matplotlib plotting

import random
import time
import csv
import sys
import matplotlib.pyplot as plt
from basic_sorts import bubble_sort, selection_sort, insertion_sort
from advanced_sorts import merge_sort, quick_sort, heap_sort

# Increase recursion limit for worst-case Quick Sort on sorted arrays
sys.setrecursionlimit(5000)

def generate_data(n, kind):
    if kind == "random":
        return [random.randint(1, 10000) for _ in range(n)]
    elif kind == "sorted":
        return list(range(1, n + 1))
    elif kind == "reverse":
        return list(range(n, 0, -1))

def main():
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort)
    ]
    sizes = [100, 400, 800, 1200]
    input_types = ["random", "sorted", "reverse"]
    results = []

    print(f"{'Algorithm':<16} | {'Input Type':<10} | {'n':<6} | {'Time (ms)':<10}")
    print("-" * 50)

    for n in sizes:
        for kind in input_types:
            base_data = generate_data(n, kind)
            for name, func in algorithms:
                start = time.perf_counter()
                func(base_data)
                elapsed_ms = (time.perf_counter() - start) * 1000
                results.append([name, kind, n, round(elapsed_ms, 4)])
                print(f"{name:<16} | {kind:<10} | {n:<6} | {elapsed_ms:<10.4f}")

    # Save raw data to CSV
    with open("timing_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Algorithm", "Input Type", "n", "Time_ms"])
        writer.writerows(results)
    print("\nSaved raw timing data to timing_results.csv")

    # Plot 1: Random Input
    plt.figure(figsize=(8, 5))
    for name, _ in algorithms:
        y_vals = [r[3] for r in results if r[0] == name and r[1] == "random"]
        plt.plot(sizes, y_vals, marker="o", label=name)
    plt.title("Sorting Algorithms Comparison (Random Input)")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.grid(True)
    plt.savefig("random_input_timing.png")
    plt.close()

    # Plot 2: Already-Sorted Input
    plt.figure(figsize=(8, 5))
    for name, _ in algorithms:
        y_vals = [r[3] for r in results if r[0] == name and r[1] == "sorted"]
        plt.plot(sizes, y_vals, marker="o", label=name)
    plt.title("Sorting Algorithms Comparison (Already-Sorted Input)")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.grid(True)
    plt.savefig("sorted_input_timing.png")
    plt.close()
    print("Saved graphs: random_input_timing.png and sorted_input_timing.png")

if __name__ == "__main__":
    main()