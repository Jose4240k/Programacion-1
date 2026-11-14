año = int(input("Dame tu año en un rango de 1900 a 2026"))

while año < 1900 or año > 2026:
    print("Error: no puedes poner un año fuera del rango de 1900 y 2026")
    año = int(input("Dame tu año en un rango de 1900 a 2026"))

mes = int(input("Dame tu mes de nacimiento en rango de 1 a 12"))

while mes < 1 or mes > 12:
    print("Error: no puedes poner un mes fuera del rango de 1 y 12")
    mes = int(input("Dame tu mes en un rango de 1 a 12"))

dia = int(input("Dame tu dia de nacimiento"))

match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        numdias = 31

    case 2:
        if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
            numdias = 29
        else:
            numdias = 28

    case 4 | 6 | 9 | 11:
        numdias = 30

while dia < 1 or dia > numdias:
    print("Error: no puedes poner un dia fuera del rango de 1 y ", numdias)
    dia = int(input("Dame tu dia de nacimiento"))

car_año = str(año)[2:]
car_mes = str(mes).zfill(2)
car_dia = str(dia).zfill(2)

fecha = car_año + car_mes + car_dia

print(fecha)