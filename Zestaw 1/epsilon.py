a = 1.0

def bisect(b):
    inf = a
    sup = b
    while sup>inf:
        n = (sup+inf)/2
        if n > a:
            sup = n
        elif n == a:
            return sup-n

print(bisect(2))