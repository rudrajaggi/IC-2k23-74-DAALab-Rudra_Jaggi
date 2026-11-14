Lab Task 1

Part 1. Trace It Yourself

Input:
List = [8, 3, 15, 6, 2]

Output:
Largest Number = 15
Sorted List = [2, 3, 6, 8, 15]

Comparisons Made:
4 comparisons to find the largest number.

Dry Run:

- i = 1: Compare 3 with 8. Maximum = 8, comparisons = 1
- i = 2: Compare 15 with 8. Maximum = 15, comparisons = 2
- i = 3: Compare 6 with 15. Maximum = 15, comparisons = 3
- i = 4: Compare 2 with 15. Maximum = 15, comparisons = 4

Sorting Method Used:
Bubble Sort

Sorting Steps:
The list is sorted by comparing adjacent elements and swapping them when they are in the wrong order. After each pass, the largest unsorted element moves to its correct position.

Explanation:
The program checks every element to find the largest number. It then sorts the list using Bubble Sort by comparing and swapping adjacent elements. Finding the maximum takes O(n) time, while Bubble Sort takes O(n²) time in the average and worst cases.

Data Structure Used:
List (Array-like structure)

Effect of Increasing Input Size:
If the input size increases 100 times, finding the maximum requires approximately 100 times as many comparisons. Bubble Sort may require approximately 10,000 times as many operations in the worst case.

Part 2. Stack or Queue

Input:
Task1, Task2, Task3, Task4, Task5

Stack Order:
Task5, Task4, Task3, Task2, Task1

Queue Order:
Task1, Task2, Task3, Task4, Task5

Printer Should Use:
Queue

Reason:
A printer should process jobs in the order they arrive. A queue follows FIFO (First In, First Out), which guarantees that the earliest task is processed first.

Dry Run:

- Stack (LIFO): Push Task1 to Task5, then remove them in reverse order.
- Queue (FIFO): Add Task1 to Task5, then remove them in the same order.

Explanation:
A stack follows LIFO, meaning the last task added is removed first. A queue follows FIFO, meaning the first task added is removed first. A queue is appropriate for a printer because it processes jobs in arrival order.

Data Structure Used:
Stack and Queue

Effect of Increasing Input Size:
If the number of tasks increases 100 times, processing all tasks takes approximately 100 times as many basic operations, assuming each insertion and removal takes O(1) time.

Part 3. Build a Small Tree

Input:
Subjects: Science, Math, Physics, Chemistry, Algebra, Geometry

Tree Drawing:

Math
|-- Algebra
|-- Geometry

Science
|-- Physics
|-- Chemistry

Output – Level Order Traversal:

Math, Science, Algebra, Geometry, Physics, Chemistry

Dry Run:

- Level 0: Math, Science
- Level 1 under Math: Algebra, Geometry
- Level 1 under Science: Physics, Chemistry
- Level order traversal: Math, Science, Algebra, Geometry, Physics, Chemistry

Explanation:
Level order traversal visits nodes level by level, starting from the top level. It visits Math and Science first, followed by their children. A queue is commonly used to implement level order traversal.

Data Structure Used:
Tree

Effect of Increasing Input Size:
If the number of nodes increases 100 times, visiting all nodes takes approximately 100 times as much work. Level order traversal takes O(n) time for n nodes.

Part 4. Count the Steps

Input:

- Single loop: i = 1 to 5
- Single loop: i = 1 to n, where n = 20
- Nested loops: i = 1 to 5 and j = 1 to 5
- Nested loops: i = 1 to n and j = 1 to n, where n = 10

Output:

- Single loop runs: 5 times
- Single loop for n = 20: 20 times
- Nested loop total prints: 25 times
- Nested loop for n = 10: 100 times

Dry Run:

- Single loop: The loop runs once for each value from 1 to 5, so it runs 5 times.
- Single loop for n = 20: The loop runs 20 times.
- Nested loop: The inner loop runs 5 times for each of the 5 outer-loop iterations. Total = 5 × 5 = 25.
- Nested loop for n = 10: Total = 10 × 10 = 100.

Explanation:
A single loop runs n times, so its time complexity is O(n), which is linear. A nested loop with both loops running n times performs n × n operations, so its time complexity is O(n²), which is quadratic.

Data Structure Used:
Loop variables and counters.

Effect of Increasing Input Size:
If n increases 100 times, a single loop performs approximately 100 times as many iterations. A nested loop performs approximately 10,000 times as many iterations.

How to Run

Run the following commands from the repository root:

python Lab1/part1_trace.py
python Lab1/part2_stack_queue.py
python Lab1/part3_tree.py
python Lab1/part4_complexity.py
