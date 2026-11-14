nombre=input("dame tu nombre")
edad = int(input("Dame tu edad"))
if not(nombre==""):
    if edad>=18 and edad<=60:
        Peso= float(input("Dame tu peso"))
        if Peso>=40 and Peso<=90:
            altura= float(input("Dame tu altura"))
            if altura>=1.5 and altura<=2.1:
                imc= Peso/(altura**2)
                print(f"Hola {nombre}, tu peso es {Peso}, tu altura es {altura} y tu imc al final es de {imc}")
                if imc<18:
                    print("peso bajo")
                elif imc>=18 and imc<=25:
                        print("Peso normal")
                else:
                            print("Sobrepeso")
else:
    print("Error: el nombre no puede quedar vacio")