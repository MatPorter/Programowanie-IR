import cmath

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

def roots(a, b, c):
    delta = b**2-4*a*c
    if delta == 0:
        print(f"x1 = {-b/(2*a)}")
    else:
        x1 = (-b-cmath.sqrt(delta))/(2*a)
        x2 = (-b+cmath.sqrt(delta))/(2*a)
        print(f"x1 = {x1}", f"x2 = {x2}", sep = '\n')

roots(a, b, c)