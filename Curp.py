
apellido1=input("Dame tu primer apellido: ")

while apellido1=="":
    print("Error: no puedes dejar este campo vacio")
    apellido1=input("Dame tu primer apellido: ")


apellido2=input("Dame tu segundo apellido: ")


nombre1=input("Dame tu primer nombre: ")

while nombre1=="":
    print("Error: no puedes dejar este campo vacio")
    nombre1=input("Dame tu primer nombre: ")


nombre2=input("Dame tu segundo nombre: ")


# ==========================================
# AÑO
# ==========================================

año=int(input("Dame tu año en un rango de 1900 a 2026: "))

while año<1900 or año>2026:
    print("Error: no puedes poner un año fuera del rango de 1900 y 2026")
    año=int(input("Dame tu año en un rango de 1900 a 2026: "))


# ==========================================
# MES
# ==========================================

mes=int(input("Dame tu mes de nacimiento en rango de 1 a 12: "))

while mes<1 or mes>12:
    print("Error: no puedes poner un mes fuera del rango de 1 y 12")
    mes=int(input("Dame tu mes en un rango de 1 a 12: "))


# ==========================================
# DIAS DEL MES
# ==========================================

match mes:

    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        numdias=31

    case 2:

        if (año%4==0 and año%100!=0) or año%400==0:
            numdias=29
        else:
            numdias=28

    case 4 | 6 | 9 | 11:
        numdias=30


# ==========================================
# DIA
# ==========================================

dia=int(input("Dame tu dia de nacimiento: "))

while dia<1 or dia>numdias:
    print("Error: no puedes poner un dia fuera del rango de 1 y",numdias)
    dia=int(input("Dame tu dia de nacimiento: "))


# ==========================================
# SEXO
# ==========================================

sexo=input("Dame tu sexo (H/M): ").upper()

while sexo!="H" and sexo!="M":
    print("Error: solamente puedes poner H o M")
    sexo=input("Dame tu sexo (H/M): ").upper()


# ==========================================
# ESTADO
# ==========================================

print("\nEstados de Mexico:")

print("AS - Aguascalientes")
print("BC - Baja California")
print("BS - Baja California Sur")
print("CC - Campeche")
print("CS - Chiapas")
print("CH - Chihuahua")
print("CL - Coahuila")
print("CM - Colima")
print("DF - Ciudad de Mexico")
print("DG - Durango")
print("GT - Guanajuato")
print("GR - Guerrero")
print("HG - Hidalgo")
print("JC - Jalisco")
print("MC - Mexico")
print("MN - Michoacan")
print("MS - Morelos")
print("NT - Nayarit")
print("NL - Nuevo Leon")
print("OC - Oaxaca")
print("PL - Puebla")
print("QT - Queretaro")
print("QR - Quintana Roo")
print("SP - San Luis Potosi")
print("SL - Sinaloa")
print("SR - Sonora")
print("TC - Tabasco")
print("TL - Tlaxcala")
print("VZ - Veracruz")
print("YN - Yucatan")
print("ZS - Zacatecas")
print("NE - Nacido en el extranjero")

estado=input("\nDame las dos letras de tu estado de nacimiento: ").upper()

while len(estado)!=2:
    print("Error: debes escribir solamente las dos letras del estado")
    estado=input("Dame las dos letras de tu estado de nacimiento: ").upper()


# ==========================================
# CONVERTIR A MAYUSCULAS
# ==========================================

apellido1=apellido1.upper()
apellido2=apellido2.upper()
nombre1=nombre1.upper()
nombre2=nombre2.upper()


# ==========================================
# QUITAR ACENTOS
# ==========================================

for letra in "ÁÉÍÓÚ":
    reemplazo="AEIOU"["ÁÉÍÓÚ".index(letra)]

    apellido1=apellido1.replace(letra,reemplazo)
    apellido2=apellido2.replace(letra,reemplazo)
    nombre1=nombre1.replace(letra,reemplazo)
    nombre2=nombre2.replace(letra,reemplazo)

apellido1=apellido1.replace("Ü","U")
apellido1=apellido1.replace("Ñ","X")
apellido2=apellido2.replace("Ü","U")
apellido2=apellido2.replace("Ñ","X")
nombre1=nombre1.replace("Ü","U")
nombre1=nombre1.replace("Ñ","X")
nombre2=nombre2.replace("Ü","U")
nombre2=nombre2.replace("Ñ","X")


# ==========================================
# PRIMERA LETRA DEL PRIMER APELLIDO
# ==========================================

car_a1=apellido1[0]


# ==========================================
# PRIMERA VOCAL INTERNA DEL PRIMER APELLIDO
# ==========================================

vocal_interna="X"

for letra in apellido1[1:]:

    if letra in "AEIOU":
        vocal_interna=letra
        break


# ==========================================
# PRIMERA LETRA DEL SEGUNDO APELLIDO
# ==========================================

if apellido2=="":
    car_a2="X"
else:
    car_a2=apellido2[0]


# ==========================================
# PRIMERA LETRA DEL NOMBRE
# ==========================================

if nombre1=="JOSE" or nombre1=="MARIA":

    if nombre2!="":
        car_n1=nombre2[0]
    else:
        car_n1=nombre1[0]

else:
    car_n1=nombre1[0]


# ==========================================
# PALABRAS INCONVENIENTES
# ==========================================

palabras_antisonantes=[
    "BACA",
    "BAKA",
    "BUEI",
    "BUEY",
    "CACA",
    "CACO",
    "CAGA",
    "CAGO",
    "CAKA",
    "COGE",
    "COGI",
    "COJA",
    "COJE",
    "COJI",
    "COJO",
    "FETO",
    "GUEI",
    "GUEY",
    "JOTO",
    "KACA",
    "KAGA",
    "KAGO",
    "KOGE",
    "KOGI",
    "KOGE",
    "KULO",
    "LOCA",
    "LOCO",
    "MAME",
    "MAMO",
    "MEAR",
    "MEAS",
    "MEON",
    "MION",
    "MOCO",
    "PEDA",
    "PEDO",
    "PENE",
    "PUTA",
    "PUTO",
    "QULO",
    "RATA",
    "RUIN",
    "SENO",
    "TETA",
    "VACA",
    "VAGA",
    "VAGO",
    "VUEI",
    "VUEY"
]


# ==========================================
# COMPROBAR PALABRA INCONVENIENTE
# ==========================================

primeros4=car_a1+vocal_interna+car_a2+car_n1

if primeros4 in palabras_antisonantes:

    vocal_interna="X"

    print("\nSe detecto una palabra inconveniente.")
    print("La segunda posicion de la CURP fue modificada.")


# ==========================================
# FECHA
# ==========================================

car_año=str(año)[2:]
car_mes=str(mes).zfill(2)
car_dia=str(dia).zfill(2)


# ==========================================
# CONSONANTE INTERNA
# ==========================================

def consonante_interna(palabra):

    for letra in palabra[1:]:

        if letra in "BCDFGHJKLMNPQRSTVWXYZ":
            return letra

    return "X"


car_c1=consonante_interna(apellido1)

if apellido2=="":
    car_c2="X"
else:
    car_c2=consonante_interna(apellido2)

car_c3=consonante_interna(nombre1)


# ==========================================
# CONSTRUIR PRIMEROS 16 CARACTERES
# ==========================================

Curp=(
    car_a1 +
    vocal_interna +
    car_a2 +
    car_n1 +
    car_año +
    car_mes +
    car_dia +
    sexo +
    estado +
    car_c1 +
    car_c2 +
    car_c3
)


# ==========================================
# CARACTER 17
# ==========================================

print("\nEl caracter 17 es asignado por RENAPO.")

if año<2000:

    caracter17=input("Dame el caracter 17 (0-9): ").upper()

    while len(caracter17)!=1 or caracter17 not in "0123456789":

        print("Error: para nacidos antes de 2000 debe ser un numero.")

        caracter17=input("Dame el caracter 17: ").upper()

else:

    caracter17=input("Dame el caracter 17 (A-J): ").upper()

    while len(caracter17)!=1 or caracter17 not in "ABCDEFGHIJ":

        print("Error: para nacidos desde 2000 debe ser una letra de A a J.")

        caracter17=input("Dame el caracter 17: ").upper()


Curp=Curp+caracter17


# ==========================================
# DIGITO VERIFICADOR
# ==========================================

tabla="0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

suma=0

for i in range(17):

    valor=tabla.index(Curp[i])

    peso=18-i

    suma=suma+(valor*peso)


digito=(10-(suma%10))%10

Curp=Curp+str(digito)


# ==========================================
# RESULTADO
# ==========================================

print("\n========================================")
print("CURP GENERADA:")
print(Curp)
print("========================================")
