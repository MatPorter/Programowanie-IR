n = int(input("n = "))

def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
        i+=1
    return fac

print(factorial(n))