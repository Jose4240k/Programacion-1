#Cifra el mensaje escrito por el usuario
minusculas = "abcdefghijklmnñopqrstuvwxyz"
mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

try:
    desplazamiento = int(input("Ingresa el desplazamiento: "))

    if desplazamiento < 0:
        print("Error: el desplazamiento debe ser positivo.")
    else:
        mensaje = input("Ingresa el mensaje: ")
        resultado = ""

        for letra in mensaje:
            if letra in minusculas:
                posicion = minusculas.index(letra)
                nueva_posicion = (posicion + desplazamiento) % len(minusculas)
                resultado += minusculas[nueva_posicion]
            elif letra in mayusculas:
                posicion = mayusculas.index(letra)
                nueva_posicion = (posicion + desplazamiento) % len(mayusculas)
                resultado += mayusculas[nueva_posicion]
            else:
                resultado += letra

        print("Mensaje cifrado:", resultado)

except ValueError:
    print("Error: debes ingresar un número entero positivo.")
