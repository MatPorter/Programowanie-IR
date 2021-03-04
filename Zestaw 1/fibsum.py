f_i_2 = 1
f_i_1 = 1
f_i = 0
i = 3
suma = 1
while f_i < 4*10**6:
    f_i = f_i_1 + f_i_2
    f_i_2 = f_i_1
    f_i_1 = f_i
    if i % 2 == 0:
        suma += f_i
    i+=1
print(suma)