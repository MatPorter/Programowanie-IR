n = int(input("n = "))

def fibonacci(n):
    f_i_2 = 1
    f_i_1 = 1
    i = 3
    if n == 1 or n == 2:
        return 1
    else:
        while i in range(3, n+1):
            f_i = f_i_1 + f_i_2
            f_i_2 = f_i_1
            f_i_1 = f_i
            i+=1
        return f_i

print(fibonacci(n))