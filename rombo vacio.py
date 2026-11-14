#Jose Miguel Valle Davila
print("Jose Miguel Valle Davila")
print("Este programa dibuja un rombo vacio, dame el tamaño en un valor de 2 a 10")
n= int(input("n="))
while n<2 or n>10:
    print("Error: el rango permitido es de 2 a 10")
    n= int(input("n="))
caracter=input("Dame el caracter a imprimir")

for i in range(1,n+1):
    espacios= " " * (n-i)
    if i ==1:
        print(espacios +caracter)
    else:
        print(espacios+caracter+" "*(2*i-3)+caracter)
for i in range(n,0,-1):
    espacios= " " * (n-i)
    print(espacios+caracter+" "*(2*i-3)+caracter)