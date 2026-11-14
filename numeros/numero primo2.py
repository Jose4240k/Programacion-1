n= int(input("n= "))
contador=0
for i in range(2,n):
    if n%i==0:
        print(i)
        print(n//i)
    contador+=1
if contador==0:
    print(f"El numero {n} es primo")
else:
    print(f"El numero {n} no es primo")