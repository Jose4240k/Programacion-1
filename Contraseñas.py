#Jose Miguel Valle Davila
print("Jose Miguel Valle Davila")
print("Este programa es un verificador de contraseñas, debes de crear una contraseña que cumpla estos criterios:")
print("1.La contraseña debe de ser de almenos 10 caracteres de longitud")
print("2.Debe de contener 1 mayuscula, una minuscula, un numero y un caracter especial")
mayuscula=0
minuscula=0
especial=0
numero=0
contra=input("Dame la contraseña a verificar")
lon=len(contra)
while lon<10:
    print("Error: La contraseña no puede ser menor a 10 caracteres")
    contra=input("Dame la contraseña a verificar")
    lon=len(contra)

for i in contra[0:]:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        mayuscula+=1
    elif i in "1234567890":
        numero+=1
    elif i in "!#$%&/()=?¡¨*][_:;><,.-}{+´¿'|°¬":
        especial+=1
    elif i in "abcdefghijklmnopqrstuvwxyz":
        minuscula+=1
                    

        
if minuscula==0:
    print("Error: debe de tener 1 minuscula")
if especial==0:
    print("Error: debe de tener 1 caracter especial")
if numero==0:
    print("Error: debe de tener 1 numero")
if mayuscula==0:
    print("Error: debe de tener 1 mayuscula")
else:
    print(f"La contraseña {contra} esta bien")
    

