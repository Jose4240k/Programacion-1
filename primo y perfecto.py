import primo as pe

n= int(input("n="))

if pe.comprobacion(n)==True:
    print(f"El numero {n} es primo")
else:
    print(f"El numero {n} no es primo")
    
if pe.perfecto(n):
    print(f"El numero {n} es perfecto")
else:
    print(f"El numero {n} no es perfecto")