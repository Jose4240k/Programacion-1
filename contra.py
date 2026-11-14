import primo as pe
c= input('Dame una contraseña')


while len(c)<10:
    print('Error este campo no puede quedar vacio')
    c= input('Dame una contraseña')
confirmacion=pe.contra(c)
print(confirmacion)