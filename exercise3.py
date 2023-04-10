age = 24
height = 185.0
complex_no = 22j

#AREA OF A TRIANGLE
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = 0.5 * base * height
print (f"The area of the triangle is, {area}")

#PERIMETER OF A TRINGLE
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))

perimeter = side_a + side_b + side_c
print (f"The perimeter of the triangle is, {perimeter}")

#AREA & PERIMETER OF A RECTANGLE
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)
print (f"The area of the rectangle is, {area}")
print (f"The perimeter of the rectangle is, {perimeter}")
