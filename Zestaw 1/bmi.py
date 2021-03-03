mass = float(input("masa = "))
height = float(input("wzrost = "))

bmi = mass/pow(height, 2)



if bmi < 18.5:
    print("niedowaga")
elif bmi <= 25:
    print("waga prawidłowa")
elif bmi <= 30:
    print("nadwaga")
else:
    print("otyłość")