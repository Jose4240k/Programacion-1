import random
maquina=random.randint(1,3)
print("elige entre estas 3 opciones"
"\n1) Piedra"
"\n2)Papel"
"\n3)Tijeras")
usuario=int(input())
if usuario<1 or usuario>3:
    print("Error no puedes elegir extra")
else:
    if (usuario==1 and maquina==3) or (usuario==2 and maquina==1) or (usuario==3 and maquina==2):
        print("Gano el usuario")
    elif (usuario==maquina):
        print("empate")
    else:
        print("Gano la maquina")