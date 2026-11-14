# Program to perform row insert, row delete, search, and 90-degree clockwise rotation on a 2D array

def print_matrix(mat):
    if len(mat) == 0:
        print("[] (Empty 2D array)")
        return
    for row in mat:
        print(row)

def insert_row(mat, pos, new_row):
    if pos < 0 or pos > len(mat):
        print("Error: Row position out of bounds.")
        return mat
    if len(mat) > 0 and len(new_row) != len(mat[0]):
        print(f"Error: Row must have {len(mat[0])} elements.")
        return mat
    mat.insert(pos, new_row)
    return mat

def delete_row(mat, pos):
    if len(mat) == 0:
        print("Error: 2D array is empty.")
        return mat
    if pos < 0 or pos >= len(mat):
        print("Error: Row position out of bounds.")
        return mat
    mat.pop(pos)
    return mat

def search_2d(mat, target):
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] == target:
                return (r, c)
    return None

def rotate_90_clockwise(mat):
    if len(mat) == 0:
        return mat
    rows = len(mat)
    cols = len(mat[0])
    rotated = []
    for c in range(cols):
        new_row = []
        for r in range(rows - 1, -1, -1):
            new_row.append(mat[r][c])
        rotated.append(new_row)
    return rotated

def main():
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    mat = []
    for i in range(r):
        while True:
            row = [int(x) for x in input(f"Enter {c} elements for row {i}: ").split()]
            if len(row) == c:
                mat.append(row)
                break
            print(f"Please enter exactly {c} numbers.")

    print("\nInitial 2D Array:")
    print_matrix(mat)

    while True:
        print("\n1. Insert Row  2. Delete Row  3. Search Value  4. Rotate 90 Clockwise  5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            pos = int(input("Enter row index to insert at: "))
            new_row = [int(x) for x in input("Enter row elements separated by space: ").split()]
            mat = insert_row(mat, pos, new_row)
            print_matrix(mat)
        elif choice == "2":
            pos = int(input("Enter row index to delete: "))
            mat = delete_row(mat, pos)
            print_matrix(mat)
        elif choice == "3":
            target = int(input("Enter value to search: "))
            res = search_2d(mat, target)
            if res:
                print(f"Found {target} at row {res[0]}, column {res[1]}.")
            else:
                print(f"Value {target} not found.")
            print_matrix(mat)
        elif choice == "4":
            mat = rotate_90_clockwise(mat)
            print("After 90-degree clockwise rotation:")
            print_matrix(mat)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()