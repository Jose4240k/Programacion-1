n= int(input("Dame un numero para ver si es perfecto"))
suma=0
for i in range(1,n):
    if n%i==0:
        suma+=i
if n==suma:
    print(f"El numero {n} es perfecto")
else:
    print(f"El numero {n} no es perfecto")