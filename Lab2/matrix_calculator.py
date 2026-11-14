# Menu-driven Matrix Calculator supporting addition, multiplication, transpose, and determinant

def input_matrix(label):
    rows = int(input(f"Enter rows for {label}: "))
    cols = int(input(f"Enter columns for {label}: "))
    if rows <= 0 or cols <= 0:
        print("Dimensions must be positive.")
        return None
    mat = []
    for i in range(rows):
        while True:
            row = [float(x) for x in input(f"Row {i}: ").split()]
            if len(row) == cols:
                mat.append(row)
                break
            print(f"Please enter {cols} numbers.")
    return mat

def print_matrix(mat):
    for row in mat:
        print([round(x, 2) if not x.is_integer() else int(x) for x in row])

def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Error: Matrices must have identical dimensions for addition.")
        return None
    res = []
    for i in range(len(a)):
        row = [a[i][j] + b[i][j] for j in range(len(a[0]))]
        res.append(row)
    return res

def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        print("Error: Columns of Matrix A must equal rows of Matrix B.")
        return None
    res = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k] * b[k][j]
    return res

def transpose_matrix(a):
    return [[a[r][c] for r in range(len(a))] for c in range(len(a[0]))]

def determinant(a):
    n = len(a)
    if n != len(a[0]):
        print("Error: Determinant is only defined for square matrices.")
        return None
    if n == 1:
        return a[0][0]
    if n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if n == 3:
        d1 = a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        d2 = a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        d3 = a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
        return d1 - d2 + d3
    # Recursive cofactor expansion for n > 3
    det = 0
    for c in range(n):
        minor = [row[:c] + row[c+1:] for row in a[1:]]
        det += ((-1) ** c) * a[0][c] * determinant(minor)
    return det

def main():
    while True:
        print("\n--- Matrix Calculator ---")
        print("1. Add two matrices")
        print("2. Multiply two matrices")
        print("3. Transpose a matrix")
        print("4. Determinant of a matrix")
        print("5. Exit")
        choice = input("Select operation: ").strip()

        if choice == "1":
            a = input_matrix("Matrix A")
            b = input_matrix("Matrix B")
            if a and b:
                res = add_matrices(a, b)
                if res:
                    print("Result:")
                    print_matrix(res)
        elif choice == "2":
            a = input_matrix("Matrix A")
            b = input_matrix("Matrix B")
            if a and b:
                res = multiply_matrices(a, b)
                if res:
                    print("Result:")
                    print_matrix(res)
        elif choice == "3":
            a = input_matrix("Matrix")
            if a:
                print("Transpose:")
                print_matrix(transpose_matrix(a))
        elif choice == "4":
            a = input_matrix("Square Matrix")
            if a:
                det = determinant(a)
                if det is not None:
                    print("Determinant:", det)
        elif choice == "5":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()