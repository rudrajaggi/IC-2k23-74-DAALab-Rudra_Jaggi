# Program to represent a subject hierarchy tree and perform level-order traversal

tree = {
    "Root": ["Math", "Science"],
    "Math": ["Algebra", "Geometry"],
    "Science": ["Physics", "Chemistry"],
    "Algebra": [],
    "Geometry": [],
    "Physics": [],
    "Chemistry": []
}

# Level order traversal using a queue
queue = []
for top_subject in tree["Root"]:
    queue.append(top_subject)

visited = []
while len(queue) > 0:
    current = queue.pop(0)
    visited.append(current)
    for child in tree[current]:
        queue.append(child)

print("Level order traversal:", visited)