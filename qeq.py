a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

def roots(a, b, c):
    delta = b**2-4*a*c
    if delta == 0:
        print(f"x1 = {-b/(2*a)}")
    elif delta > 0:
        x1 = (-b-delta)/(2*a)
        x2 = (-b+delta)/(2*a)
        print(f"x1 = {x1}", f"x2 = {x2}", sep = '\n')
    else:
        print("Nie ma rozwiązań")

roots(a, b, c)