# write a script that prompts the user to enter base and height of the triangle and calculate an area of the triangle (Area = 0.5*b*h)

b = float(input("Enter the Base "))
h = float(input("Enter the height "))

#area = 0.5 * b * h
#print("The area of the triangle is :", area)


def area(b, h):
    a = 0.5 * b * h
    return a


print(area(b, h))
