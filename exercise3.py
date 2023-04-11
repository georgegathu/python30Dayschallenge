# QUIZ 1:
age = 24
height = 185.0
complex_no = 22j

#QUIZ 2: AREA OF A TRIANGLE
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = 0.5 * base * height
print (f"The area of the triangle is, {area}")

#QUIZ 3: PERIMETER OF A TRINGLE
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))

perimeter = side_a + side_b + side_c
print (f"The perimeter of the triangle is, {perimeter}")

#QUIZ 4: AREA & PERIMETER OF A RECTANGLE
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)
print (f"The area of the rectangle is, {area}")
print (f"The perimeter of the rectangle is, {perimeter}")

# QUIZ 5: Calculate the area of a circle
pi = 3.14
radius = float(input("Input radius of the circle: "))
area = pi * radius * radius
print (f"The area of the Circle is: {area}")

# Quiz 8: Calculate the slope
# Define the equation
eq = "y = 2x - 2"
# Extract the coefficients
coeffs = eq.split()[2:]
m = float(coeffs[0])
b = float(coeffs[1])
# Calculate the slope
slope = m
# Calculate the x-intercept
x_intercept = -b/m
# Calculate the y-intercept
y_intercept = b
# Print the results
print("Slope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

# QUIZ 9:
# Define the coordinates of the points
x1, y1 = 2, 2
x2, y2 = 6, 10
# Calculate the slope
m = (y2 - y1) / (x2 - x1)
# Calculate the Euclidean distance
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# Print the results
print("Slope:", m)
print("Euclidean distance:", distance)