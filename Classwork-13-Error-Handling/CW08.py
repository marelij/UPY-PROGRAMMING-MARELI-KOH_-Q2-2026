import math

# input
a = input("write the left endpoint of the interval: ")
b = input("write the right endpoint of the interval: ")
f_x = input("write the function to integrate: ")
method = input("Write the integration method (LRM/RRM/MRM/TRAP): ")

# process
try:
    # ---------- ENDPOINTS ----------
    if "pi" in a:
        a = eval(a.replace("pi", str(math.pi)))
    else:
        a = float(a)

    if "pi" in b:
        b = eval(b.replace("pi", str(math.pi)))
    else:
        b = float(b)

except ValueError:
    print("The endpoints must be valid numbers")
    raise SystemExit

except (SyntaxError, NameError):
    print("Invalid expression in the endpoint")
    raise SystemExit

try:
    # ---------- BUSINESS RULES ----------

    if a >= b:
        raise ValueError("The left endpoint must be less than the right endpoint")

    if method not in ["LRM", "RRM", "MRM", "TRAP"]:
        raise ValueError("Invalid integration method")

    if f_x.strip() == "":
        raise ValueError("The function cannot be empty")

    if "x" not in f_x:
        raise ValueError("The function must be written in terms of x")

    if "^" in f_x:
        raise SyntaxError

except ValueError as e:
    print(e)
    raise SystemExit

except SyntaxError:
    print("Invalid function expression")
    raise SystemExit

n = 1000
h = (b - a) / n
area = 0.0
constant = 0
shift = 0
variable = 0

if method == "RRM":
    shift = 1

if method == "MRM":
    constant = h / 2

try:

    # Verificar que la función esté definida en el intervalo
    for punto in [a, (a+b)/2, b]:
        prueba = f_x.replace("x", str(punto))
        eval(prueba)

    if method == "TRAP":

        variable = 1

        f_0 = f_x.replace("x", str(a))
        area += (h / 2) * eval(f_0)

        for i in range(variable, n):

            xi = a + i * h
            f_xi = f_x.replace("x", str(xi))
            area += (h / 2) * 2 * eval(f_xi)

        f_xn = f_x.replace("x", str(b))
        area += (h / 2) * eval(f_xn)

    else:

        for i in range(shift, n + shift):

            xi = a + i * h
            height = f_x.replace("x", str(xi + constant))
            area += h * eval(height)

except ZeroDivisionError:
    print("The function is not defined somewhere in the interval")
    raise SystemExit

except (SyntaxError, NameError):
    print("Invalid function expression")
    raise SystemExit

except ValueError:
    print("Math domain error")
    raise SystemExit

else:
    # output
    print(f"The integration of {f_x} is {area:.3f}")