# Lab Task 2

## Part 1. Trace It Yourself
Input: [8, 3, 15, 6, 2]
Output: Largest number = 15, Sorted list = [2, 3, 6, 8, 15]
Comparisons made: 4
Dry Run:
i=1 A[i]=3, max=8, comparisons=1
i=2 A[i]=15, max=15, comparisons=2
i=3, A[i]=6, max=15, comparisons=3
i=4, A[i]=2, max=15, comparisons=4
Sorting method used: Selection Sort
Sorting steps:
Step 1: [2, 3, 15, 6, 8]
Step 2: [2, 3, 15, 6, 8]
Step 3: [2, 3, 6, 15, 8]
Step 4: [2, 3, 6, 8, 15]
Data structure used: 1D List (Array)
Growth if input size grew 100x: Finding the max grows proportionally (100x work, O(n)), while sorting grows explosively (10,000x work, O(n^2)).
Explanation:
The code assumes the first element is the maximum and scans through the rest of the list one by one, updating max whenever a larger number appears. Because the list is unsorted, every element must be checked at least once so we do not miss the largest value.

## Part 2. Stack or Queue
Input: Task1, Task2, Task3, Task4, Task5
Stack order: Task5, Task4, Task3, Task2, Task1
Queue order: Task1, Task2, Task3, Task4, Task5
Printer should use: Queue
Reason: A printer must process jobs in the exact order they were submitted (First-In, First-Out).
Dry Run:
Stack (LIFO): push Task1, Task2, Task3, Task4, Task5 then pop in reverse -> Task5, Task4, Task3, Task2, Task1
Queue (FIFO): enqueue Task1 to Task5 then dequeue in same order -> Task1, Task2, Task3, Task4, Task5
Data structure used: Stack and Queue (implemented via Python lists)
Growth if input size grew 100x: Effort grows proportionally (100x) because each task is pushed/enqueued and popped/dequeued once.
Explanation:
A printer needs first-come, first-served order so that users who sent documents earlier do not wait behind newer print jobs. A Queue guarantees this behavior because items are removed from the front in the same order they entered from the back.

## Part 3. Build a Small Tree
Input: Subjects (Math, Science, Physics, Chemistry, Algebra, Geometry)
Output: Math, Science, Algebra, Geometry, Physics, Chemistry
Tree Structure:

[Root]
  /    \
Math    Science
/  \      /

Alg. Geom. Phys. Chem.

Dry Run:
Level 0: Math, Science
Level 1 under Math: Algebra, Geometry
Level 1 under Science: Physics, Chemistry
Level order traversal: Math -> Science -> Algebra -> Geometry -> Physics -> Chemistry
Data structure used: Tree (Dictionary adjacency list) and Queue for traversal
Growth if input size grew 100x: Effort grows proportionally (100x) because each node in the tree is visited once.
Explanation:
Level-order traversal visits all nodes at the current depth before moving down to the next level. Using a queue ensures that parent nodes discovered first have their children visited in the same left-to-right order.

## Part 4. Count the Steps
Input: Loop limits n = 5, 10, 20
Single loop runs: 5 (for n=20, it runs 20 times)
Nested loop total prints: 25 (for n=10, it runs 100 times)
Dry Run:
Single loop, i=1 to 5, prints 5 times
Nested loop, i=1 to 5 and j=1 to 5, inner print runs 5 times for each i, total 25 times
For n=10:
Single loop runs: 10
Nested loop runs: 100
Data structure used: None (simple loop counters)
Growth if input size grew 100x: The single loop grows proportionally (100x), whereas the nested loop grows explosively (10,000x).
Explanation:
The single loop executes once per item, so doubling the input doubles the work (linear O(n) growth). The nested loop runs a full inner loop for every single step of the outer loop, causing total operations to grow quadratically (O(n^2)).

## How to run
python part1_trace.py
python part2_stack_queue.py
python part3_tree.py
python part4_complexity.py