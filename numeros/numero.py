cadena= input("Ingresa la frase")
cadena_s_espacios=cadena.replace(" ","")
alrevez= cadena_s_espacios[::-1]
print("Cadena original: ",cadena)
print("Cadena sin espacios:", cadena_s_espacios)
print("Al revez: ",alrevez)

if alrevez==cadena_s_espacios:
    print(f"la frase {cadena} es palindroma")
else:
    print(f"la frase {cadena} no es palindroma")