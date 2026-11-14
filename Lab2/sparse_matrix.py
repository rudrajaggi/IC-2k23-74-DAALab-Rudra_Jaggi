# Program to convert, reconstruct, and add matrices in sparse triple representation

def to_sparse(matrix):
    triples = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != 0:
                triples.append((r, c, matrix[r][c]))
    return triples

def to_full(triples, rows, cols):
    full = [[0 for _ in range(cols)] for _ in range(rows)]
    for r, c, val in triples:
        full[r][c] = val
    return full

def add_sparse(sparse_a, sparse_b):
    # Store entries in a dictionary keyed by (row, col) to add without full reconstruction
    combined = {}
    for r, c, val in sparse_a:
        combined[(r, c)] = combined.get((r, c), 0) + val
    for r, c, val in sparse_b:
        combined[(r, c)] = combined.get((r, c), 0) + val

    result = []
    for (r, c) in sorted(combined.keys()):
        if combined[(r, c)] != 0:
            result.append((r, c, combined[(r, c)]))
    return result

def read_matrix(name, rows, cols):
    print(f"Enter elements for Matrix {name} ({rows}x{cols}):")
    mat = []
    for i in range(rows):
        while True:
            row = [int(x) for x in input(f"Row {i}: ").split()]
            if len(row) == cols:
                mat.append(row)
                break
            print(f"Enter exactly {cols} integers.")
    return mat

def main():
    rows = int(input("Enter number of rows for matrices: "))
    cols = int(input("Enter number of columns for matrices: "))
    if rows <= 0 or cols <= 0:
        print("Error: Dimensions must be positive.")
        return

    mat_a = read_matrix("A", rows, cols)
    mat_b = read_matrix("B", rows, cols)

    sparse_a = to_sparse(mat_a)
    sparse_b = to_sparse(mat_b)

    print("\nMatrix A Sparse Form (row, col, val):", sparse_a)
    print(f"Storage -> Full: {rows * cols} values | Sparse: {len(sparse_a) * 3} values")
    print("Reconstructed Matrix A:")
    for row in to_full(sparse_a, rows, cols):
        print(row)

    print("\nMatrix B Sparse Form (row, col, val):", sparse_b)
    print(f"Storage -> Full: {rows * cols} values | Sparse: {len(sparse_b) * 3} values")

    sparse_sum = add_sparse(sparse_a, sparse_b)
    print("\nSum in Sparse Form:", sparse_sum)
    print("Reconstructed Sum Matrix:")
    for row in to_full(sparse_sum, rows, cols):
        print(row)

if __name__ == "__main__":
    main()