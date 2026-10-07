students = {
    101: ("Ishita", "CSE", 85),
    102: ("Surabhi", "AI", 90),
    103: ("Aryan", "CSE", 78)
}

students[104] = ("Rahul", "DS", 88)

del students[103]

students[102] = ("Surabhi", "AI", 95)

print("Final Student Records:")

for roll, details in students.items():
    print("Roll Number:", roll)
    print("Name:", details[0])
    print("Branch:", details[1])
    print("Marks:", details[2])
    print()
