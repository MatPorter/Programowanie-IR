import timeit

a = float(input("a = "))
b = float(input("b = "))

mult = timeit.Timer(lambda: a*b)
summ = timeit.Timer(lambda: a+b)
print(mult.timeit())
print(summ.timeit())
print(summ.timeit()-mult.timeit())