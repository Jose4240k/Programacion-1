numero=int(input("Dame el numero a buscar sus divisores"))
for i in range(1,numero+1):
    if numero%i ==0:
        print(f"{i} es un numero divisor de {numero}")