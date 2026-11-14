# Search Engine Simulator comparing Binary Search, Hash Table (Chaining), and Hash Table (Linear Probing)

def custom_hash(word, table_size):
    total = 0
    for i, ch in enumerate(word):
        total += (i + 1) * ord(ch)
    return total % table_size

class HashChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, val):
        idx = custom_hash(key, self.size)
        self.table[idx].append((key, val))

    def search(self, key):
        idx = custom_hash(key, self.size)
        comparisons = 0
        for k, v in self.table[idx]:
            comparisons += 1
            if k == key:
                return v, comparisons
        return None, comparisons

class HashLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key, val):
        idx = custom_hash(key, self.size)
        for _ in range(self.size):
            if self.table[idx] is None:
                self.table[idx] = (key, val)
                return
            idx = (idx + 1) % self.size

    def search(self, key):
        idx = custom_hash(key, self.size)
        probes = 0
        for _ in range(self.size):
            probes += 1
            if self.table[idx] is None:
                return None, probes
            if self.table[idx][0] == key:
                return self.table[idx][1], probes
            idx = (idx + 1) % self.size
        return None, probes

def binary_search_words(sorted_items, target):
    low, high = 0, len(sorted_items) - 1
    comparisons = 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if sorted_items[mid][0] == target:
            return sorted_items[mid][1], comparisons
        elif sorted_items[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None, comparisons

def main():
    vocabulary = {
        "algorithm": 12, "array": 25, "binary": 18, "bucket": 7, "cache": 14,
        "collision": 9, "compile": 11, "data": 40, "debug": 16, "dynamic": 10,
        "element": 22, "function": 30, "graph": 19, "hash": 27, "heap": 15,
        "index": 33, "iterate": 8, "key": 29, "linear": 13, "list": 35,
        "loop": 21, "matrix": 17, "memory": 24, "merge": 12, "node": 26,
        "pivot": 6, "pointer": 14, "queue": 20, "radix": 5, "recursion": 18,
        "search": 31, "sort": 38, "stack": 23, "tree": 28, "variable": 19
    }

    sorted_list = sorted(vocabulary.items())
    table_size = 43  # Prime size > 35 words (~81% load factor)
    chaining_ht = HashChaining(table_size)
    probing_ht = HashLinearProbing(table_size)

    for word, freq in vocabulary.items():
        chaining_ht.insert(word, freq)
        probing_ht.insert(word, freq)

    while True:
        query = input("\nEnter word to search (or 'exit' to quit): ").strip().lower()
        if query == "exit":
            break

        val_b, steps_b = binary_search_words(sorted_list, query)
        val_c, steps_c = chaining_ht.search(query)
        val_p, steps_p = probing_ht.search(query)

        if val_b is not None:
            print(f"Word '{query}' FOUND (Frequency: {val_b})")
        else:
            print(f"Word '{query}' NOT FOUND")

        print(f"  1. Binary Search          -> {steps_b} comparisons")
        print(f"  2. Hash (Chaining)        -> {steps_c} comparisons")
        print(f"  3. Hash (Linear Probing)  -> {steps_p} probes")

if __name__ == "__main__":
    main()