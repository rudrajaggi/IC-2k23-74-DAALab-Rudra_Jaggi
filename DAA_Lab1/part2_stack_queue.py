# Program to demonstrate Stack (LIFO) and Queue (FIFO) task execution

tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]

# Stack implementation using a Python list
stack = []
for t in tasks:
    stack.append(t)

stack_order = []
while len(stack) > 0:
    stack_order.append(stack.pop())

print("Stack completion order (LIFO):", stack_order)

# Queue implementation using a Python list
queue = []
for t in tasks:
    queue.append(t)

queue_order = []
while len(queue) > 0:
    queue_order.append(queue.pop(0))

print("Queue completion order (FIFO):", queue_order)
print("Printer should use: Queue")
print("Printer print order:", queue_order)