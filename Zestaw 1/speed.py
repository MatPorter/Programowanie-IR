import time

a = float(input("a = "))
b = float(input("b = "))

add_start = time.perf_counter_ns()
c = a + b
add_stop = time.perf_counter_ns()

mul_start = time.perf_counter_ns()
c = a * b
mul_stop = time.perf_counter_ns()

print(f"Dodawanie: {add_stop - add_start}")
print(f"Mnożenie: {mul_stop - mul_start}")
print(f"Różnica: {(mul_stop - mul_start) - (add_stop - add_start)}"")