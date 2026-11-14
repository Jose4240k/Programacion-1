Mes=int(input("Dame el mes en el que naciste"))
Dia=int(input("Dame el dia en el que naciste"))
Año=int(input("Dame el año en el que naciste"))
a = (14 - Mes) // 12
b = Año - a
c = Mes + (12*a) - 2

indicador = Dia + b + (b // 4) - (b // 100) + (b // 400) + (31 * c) // 12
 
resultado = indicador % 7
 
if resultado == 0:
    print("El día es Domingo")
elif resultado == 1:
    print("El día es Lunes")
elif resultado == 2:
    print("El día es Martes")
elif resultado == 3:
    print("El día es Miércoles")
elif resultado == 4:
    print("El día es Jueves")
elif resultado == 5:
    print("El día es Viernes")
else:
    print("El día es Sábado")