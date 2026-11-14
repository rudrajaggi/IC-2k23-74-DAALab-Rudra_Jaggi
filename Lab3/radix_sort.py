# LSD Radix Sort for non-negative integers using Counting Sort as a helper

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    return output

def radix_sort(arr):
    if len(arr) <= 1:
        return arr.copy()
    a = arr.copy()
    max_val = max(a)
    exp = 1
    while max_val // exp > 0:
        a = counting_sort_by_digit(a, exp)
        exp *= 10
    return a

if __name__ == "__main__":
    sample = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original array:", sample)
    print("Radix Sorted:  ", radix_sort(sample))