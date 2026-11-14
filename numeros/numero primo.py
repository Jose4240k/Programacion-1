numero=int(input("Dame el numero a buscar sus divisores"))
contador=0
for i in range(2,numero):
    if numero%i ==0:
        print(f"{i} es un numero divisor de {numero}")
        contador+=1
        
if contador==0:
    print(f"el numero {numero} es primo")