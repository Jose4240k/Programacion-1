import primo as pe
n=int(input("n= "))
ind= pe.comprobacion(n)

if ind==0:
    print(f"el numero {n} es primo")
else:
    print(f"el numero {n} no es primo")