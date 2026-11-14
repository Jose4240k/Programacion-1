positivo=0
negativo=0
cero=0
for i in range(1,11):
    numero= int(input(f"Dame el numero {i} a analizar"))
    if numero>0:
        positivo+=1
    elif numero==0:
        cero+=1
    elif numero<0:
        negativo+=1
print(f"De los 10 numero a buscar, encontre {positivo} positivos {cero} ceros y {negativo} negativos")