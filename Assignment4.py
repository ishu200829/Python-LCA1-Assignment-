rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

A = []
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(int(input("Enter element: ")))
    A.append(row)

B = []
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(int(input("Enter element: ")))
    B.append(row)

C = []

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Sum of the two matrices:")

for row in C:
    print(row)
