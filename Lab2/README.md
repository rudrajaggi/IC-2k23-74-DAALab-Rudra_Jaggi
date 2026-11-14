# DAA Lab 2 - Python Programs

## Program 1: 1D Array Operations

### Aim
To perform basic operations on a 1D array using Python, including insertion, deletion, linear search, and left/right rotation.

### Logic
The program uses a Python list to represent a 1D array. Separate functions are used for insertion, deletion, linear search, and left/right rotation. Index bounds are checked before performing insertion and deletion.

### Sample Input / Output

Initial Array:

10 20 30 40 50

After inserting 25 at index 2:

[10, 20, 25, 30, 40, 50]

After deleting the element at index 0:

[20, 25, 30, 40, 50]

After searching for 30:

Value found at index: 2

After left rotation by 2 positions:

[30, 40, 50, 20, 25]

After right rotation by 2 positions:

[20, 25, 30, 40, 50]

Boundary Case:

For an invalid index, the program displays:

Invalid index.


---

## Program 2: 2D Array Operations

### Aim
To perform insertion, deletion, searching, and 90-degree clockwise rotation operations on a 2D array.

### Logic
The program represents a 2D array using a list of lists. Separate functions are used to insert and delete rows, search for a value, and rotate the complete array 90 degrees clockwise.

### Sample Input / Output

Initial Matrix:

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

After inserting the row [10, 11, 12] at position 1:

[1, 2, 3]
[10, 11, 12]
[4, 5, 6]
[7, 8, 9]

After searching for value 5:

Value found at row 2 and column 1

After 90-degree clockwise rotation:

[7, 4, 10, 1]
[8, 5, 11, 2]
[9, 6, 12, 3]

Boundary Case:

For an invalid row position, the program displays:

Invalid position.


---

## Program 3: Sparse Matrix Representation and Operations

### Aim
To convert a full 2D matrix into sparse triple representation, reconstruct the full matrix, and add two matrices while both are in sparse form.

### Logic
The program stores every non-zero element using its row, column, and value. The first row of the sparse representation stores the number of rows, columns, and non-zero elements. Two sparse matrices are added by comparing their row and column positions without converting them back to full matrices.

### Sample Input / Output

Boundary Case:

Input:
Rows = 2
Columns = 2

Matrix:
0 0
0 0

Output:
Sparse representation:
(2, 2, 0)

The matrix contains no non-zero elements.
#### First Matrix

[1, 0, 0, 0, 0, 0]
[0, 2, 0, 0, 0, 0]
[0, 0, 3, 0, 0, 0]
[0, 0, 0, 4, 0, 0]
[0, 0, 0, 0, 5, 0]
[0, 0, 0, 0, 0, 6]

Number of non-zero elements = 6

Sparse representation:

[6, 6, 6]
[0, 0, 1]
[1, 1, 2]
[2, 2, 3]
[3, 3, 4]
[4, 4, 5]
[5, 5, 6]

#### Second Matrix

[1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]

Number of non-zero elements = 1

Sparse representation:

[6, 6, 1]
[0, 0, 1]

#### Addition Result

Sparse representation:

[6, 6, 6]
[0, 0, 2]
[1, 1, 2]
[2, 2, 3]
[3, 3, 4]
[4, 4, 5]
[5, 5, 6]

Reconstructed full matrix:

[2, 0, 0, 0, 0, 0]
[0, 2, 0, 0, 0, 0]
[0, 0, 3, 0, 0, 0]
[0, 0, 0, 4, 0, 0]
[0, 0, 0, 0, 5, 0]
[0, 0, 0, 0, 0, 6]


### Space Optimization Analysis

For an m x n matrix containing k non-zero elements:

Full 2D representation:

O(m x n)

Sparse triple representation:

O(k)

For the 6 x 6 test matrices:

Total elements = 6 x 6 = 36

#### Matrix 1

Zero elements = 30

Non-zero elements = 6

Full 2D representation stores 36 values.

Sparse representation contains 6 non-zero entries plus 1 header row.

#### Matrix 2

Zero elements = 35

Non-zero elements = 1

Full 2D representation stores 36 values.

Sparse representation contains 1 non-zero entry plus 1 header row.

### Approximate Break-Even Point

Each sparse entry stores three values: row, column, and value.

Ignoring the header, the approximate break-even point is:

3k = m x n

For a 6 x 6 matrix:

3k = 36

k = 12

Therefore, the approximate break-even point is about 12 non-zero elements, or about 33% of the matrix elements.

### Real-World Example

Graph adjacency matrices can naturally be sparse. When a graph has relatively few connections, most entries of the adjacency matrix are zero.


---

## Program 4: Matrix Calculator

### Aim
To create a menu-driven matrix calculator that performs matrix addition, multiplication, transpose, and determinant calculation.

### Logic
The program takes matrix dimensions and elements as input. It validates matrix dimensions before addition and multiplication. Determinant calculation is performed only for square matrices. Determinants of 1x1, 2x2, and 3x3 matrices are supported.

### Sample Input / Output

#### Matrix Addition

First Matrix:

[1, 2]
[3, 4]

Second Matrix:

[5, 6]
[7, 8]

Addition Result:

[6, 8]
[10, 12]

#### Transpose

For the matrix:

[1, 2]
[3, 4]

Transpose:

[1, 3]
[2, 4]

#### Determinant

For the matrix:

[1, 2]
[3, 4]

Determinant = -2

Boundary Case:

If matrices have incompatible dimensions for addition, the program displays:

Addition not possible: dimensions are different.

For multiplication, the number of columns of the first matrix must equal the number of rows of the second matrix.


---

## Conclusion

These programs demonstrate basic 1D array, 2D array, sparse matrix, and matrix calculator operations using Python.

The programs use separate functions, input validation, and menu-driven operations where required.
