#4. write a script that prompts user to enter side a,b,c of a triangle.calculate the perimeter of the triangle
#perimeter = a+b+c
a = int(input("Enter the side a :"))
b = int(input("Enter the side b :"))
c = int(input("Enter the side c :"))


def perimeter(a, b, c):
    answer = a + b + c
    return answer


print(perimeter(a, b, c))
