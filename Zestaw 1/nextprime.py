import numpy
import math

n = int(input("n = "))

def sieve(n):
    if n < 2:
        return False
    else:
        k = 0
        i=2
        while i <= math.ceil(numpy.sqrt(n+k)):
            if (n+k) % i == 0:
                k += 1
                i = 2
            else:
                i += 1
    return n+k

print(sieve(n))