# Anthony Camara- hernandez 
# 4/12/2026
# P2LAB1
#Using the radius, which should be given by the user as a float, the program will calculate the diameter, circumference, and area of a circle.

# Import math mofule to use the constant, math. pi

import math

# Ger radius form user

radius = float (input("What is the radius of the circle? "))
print()

#calculate diameter
diameter = 2 * radius 

#Display diameter
print(f"the diamter of the circle is {diameter:.1f}\n")

#Calculate circumference
circumference = 2 * math.pi * radius

#Display circumference with decminal places
print(f"The circumference of the circle is {circumference:.2f}\n")

#calculate the are
area = math.pi * radius**2

#Display area with 3 decimal places
print(f"The are of the circle is {area:.3f}")

