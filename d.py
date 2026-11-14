m = int(input("Ingrese la cantidad de renglones (m): "))

# Parte superior (creciente)
for i in range(1, m + 1):
    print(" " * (m - i) + "*" * i)
# Parte inferior (decreciente)
for i in range(m - 1, 0, -1):
    print(" " * (m - i) + "*" * i)

# Parte superior (creciente)
for i in range(1, m + 1):
    print("*" * i)
# Parte inferior (decreciente)
for i in range(m - 1, 0, -1):
    print("*" * i)






