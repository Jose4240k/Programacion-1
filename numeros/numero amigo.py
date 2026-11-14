n = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))

suma = 0
suma2 = 0

# Suma de divisores propios del primer número (de 1 hasta n-1)
for i in range(1, n):
    if n % i == 0:
        suma += i

# Suma de divisores propios del segundo número (de 1 hasta n2-1)
for i in range(1, n2):
    if n2 % i == 0:
        suma2 += i

# Verificación de la condición de números amigos
if suma == n2 and suma2 == n:
    print(f"Los numeros {n} y {n2} son amigos")
else:
    print(f"Los numeros {n} y {n2} no son amigos")