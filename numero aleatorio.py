import random

minimo = 1
maximo = 100

n = int(input("Dame un numero inicial para jugar del 1 al 100: "))
r = random.randint(1, 100)
c = 0

while not (n == r) and c < 5:
    if n > r:
        print("El numero magico es menor que", n)
        maximo = n - 1
    elif n < r:
        print("El numero magico es mayor que", n)
        minimo = n + 1

    c += 1

    if c < 5:
        print("El nuevo rango es de", minimo, "a", maximo)
        n = int(input("Dame un numero dentro del nuevo rango: "))

if n == r:
    print("Le atinaste")
elif c == 5:
    print("Superaste la cantidad de intentos permitidos, perdiste el juego, el numero es: ",r)
    