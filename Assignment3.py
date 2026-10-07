def right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if right_triangle(a, b, c):
    print("It is a right-angled triangle")
else:
    print("It is not a right-angled triangle")
