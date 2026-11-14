numero= int(input(f"Dame el numero a analizar"))
mayor=numero
menor=numero
for i in range(1,11):
    numero= int(input(f"Dame el numero {i} a analizar"))
    if numero>=mayor:
        mayor=numero
    elif numero<=menor:
        menor=numero
print(f"El numero mayor es {mayor} y el numero menor es {menor}")