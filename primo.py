def comprobacion(n):
    divisores=0
    for i in range(2,n):
        if n%i==0:
            divisores+=1
    if divisores==0:
        return True
    else:
        return False
def dia(d):
    if d==1:
        dia="Lunes"
    elif d==2:
        dia="Martes"
    elif d==3:
        dia="Miercoles"
    elif d==4:
        dia="Jueves"
    elif d==5:
        dia="Viernes"
    elif d==6:
        dia="Sabado"
    elif d==7:
        dia="Domingo"
    return dia

def mayortres(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        return "Todos son iguales"
    
def mayordos(a,b):
    if a>b:
        return "El mayor es a"
    elif b>a:
        return "El mayot es b"
    else:
        return "Son iguales"
    
def curp(n1,n2,a1,a2):
    curp= a1[0:2]
    if a2!="":
        curp= curp+a2[0]
    else:
        curp= curp+"X"
        
    if(n1=="JOSE" or n1=="J." or n1=="J" or n1=="MARIA" or n1=="M." or n1=="M") and len(n2)>0:
        curp= curp
        
def diames(a,m,d):
    match m:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            numdias = 31

        case 2:
            if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
                numdias = 29
            else:
                numdias = 28

        case 4 | 6 | 9 | 11:
            numdias = 30
    if d>numdias:
        return "el dia esta fuera del rango"
    else:
        fecha= f"{d} de {m} del año {a}"
        return
    
def contra(c):
    mayuscula=0
    numero=0
    especial=0
    minuscula=0
    for i in c[0:]:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            mayuscula+=1
        if i in "1234567890":
            numero+=1
        if i in "!#$%&/()=?¡¨*][_:;><,.-}{+´¿'|°¬":
            especial+=1
        if i in "abcdefghijklmnopqrstuvwxyz":
            minuscula+=1
                    

        
    if minuscula==0:
        return "Error: debe de tener 1 minuscula"
    if especial==0:
        return "Error: debe de tener 1 caracter especial"
    if numero==0:
        return "Error: debe de tener 1 numero"
    if mayuscula==0:
        return "Error: debe de tener 1 mayuscula"
    else:
        return f"La contraseña esta bien"
        
def perfecto(n):
    suma=0
    for i in range(1,n):
        if n%i==0:
            suma+=i
            
        if suma==n:
            return f"El numero {n} es perfecto"
  