# Program to count loop iterations for single and nested loops

# Single loop 1 to 5
count1 = 0
for i in range(1, 6):
    count1 += 1
print("Single loop (1 to 5) runs:", count1)

# Single loop n = 20
n = 20
count_n20 = 0
for i in range(1, n + 1):
    count_n20 += 1
print("Single loop (n=20) runs:", count_n20)

# Nested loop 1 to 5
count2 = 0
for i in range(1, 6):
    for j in range(1, 6):
        count2 += 1
print("Nested loop (1 to 5) total prints:", count2)

# Nested loop n = 10
n = 10
count_n10 = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        count_n10 += 1
print("Nested loop (n=10) total prints:", count_n10)