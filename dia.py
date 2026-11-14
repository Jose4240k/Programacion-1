import primo as pe
d=int(input("Dame el numero de dia de la semana entre el 1 al 7"))

while d<1 or d>7:
    print("el numero de dia debe de ser entre 1 a 7")
    d=int(input("Dame el numero de dia de la semana entre el 1 al 7"))

ind=pe.dia(d)

print(ind)