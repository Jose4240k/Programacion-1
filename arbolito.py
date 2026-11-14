m=int(input("Cantidad de renglones a imprimir con asteriscos"))

for i in range(1,m+1):
    for j in range(1,i+1):
        print("*",end="")
    print()