# INPUT
import math

# Get the left and right endpoints from the user
a = input("Write the left endpoint of the interval: ")
b = input("Write the right endpoint of the interval: ")

# Get the function and method from the user
f_x = input("Write the function to integrate: ")
method = input("Write the integration method (LRM/RRM/MRM/TRAP): ")

# PROCESS

# Check if 'pi' is in the left endpoint and replace it with its value
if "pi" in a:
    a = eval(a.replace("pi", str(math.pi)))
else:
    a = float(a)

# Check if 'pi' is in the right endpoint and replace it with its value
if "pi" in b:
    b = eval(b.replace("pi", str(math.pi)))
else:
    b = float(b)

# Initialize variables for the integration
n = 1000           # Number of intervals
h = (b - a) / n   # Width of each interval
area = 0.0         # Accumulated area
Shift = 0          # Used by RRM to shift one step right
Constant = 0       # Used by MRM to evaluate at midpoint
variable = 0       # Used by TRAP as starting index

# Set shift for Right Riemann Method
if method == "RRM":
    Shift = 1

# Set constant for Midpoint Riemann Method
if method == "MRM":
    Constant = h / 2

# Trapezoidal Rule: first term + middle terms + last term
if method == "TRAP":
    variable = 1
    f_0 = f_x.replace("x", str(a))
    area += (h / 2) * eval(f_0)  # First term

    for i in range(variable, n):
        xi = a + i * h
        f_xi = f_x.replace("x", str(xi))
        area += (h / 2) * 2 * eval(f_xi)  # Middle terms

    f_xn = f_x.replace("x", str(b))
    area += (h / 2) * eval(f_xn)  # Last term

else:
    # General loop for LRM, RRM and MRM
    for i in range(Shift, n + Shift):
        xi = a + i * h
        height = f_x.replace("x", str(xi + Constant))
        area += h * eval(height)  # Add rectangle area

# OUTPUT
print(f"the integration of {f_x} is: {area}")