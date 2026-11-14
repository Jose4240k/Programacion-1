
estados = {
    "Aguascalientes": "AS",
    "Baja California": "BC",
    "Baja California Sur": "BS",
    "Campeche": "CC",
    "Coahuila": "CL",
    "Colima": "CM",
    "Chiapas": "CS",
    "Chihuahua": "CH",
    "Ciudad de México": "DF",
    "Durango": "DG",
    "Guanajuato": "GT",
    "Guerrero": "GR",
    "Hidalgo": "HG",
    "Jalisco": "JC",
    "Estado de México": "MC",
    "Michoacán": "MN",
    "Morelos": "MS",
    "Nayarit": "NT",
    "Nuevo León": "NL",
    "Oaxaca": "OC",
    "Puebla": "PL",
    "Querétaro": "QT",
    "Quintana Roo": "QR",
    "San Luis Potosí": "SP",
    "Sinaloa": "SL",
    "Sonora": "SR",
    "Tabasco": "TC",
    "Tamaulipas": "TS",
    "Tlaxcala": "TL",
    "Veracruz": "VZ",
    "Yucatán": "YN",
    "Zacatecas": "ZS",
    "Nacido en el extranjero": "NE"
}

print("LISTA DE ENTIDADES Y CLAVES")
for estado, clave in estados.items():
    print(estado, "-", clave)

nombre = input("\nNombre(s): ").strip().upper()
paterno = input("Apellido paterno: ").strip().upper()
materno = input("Apellido materno (si no tienes, escribe X): ").strip().upper()

print("\nFECHA DE NACIMIENTO")
dia = input("Día (DD): ").strip()
mes = input("Mes (MM): ").strip()
anio = input("Año (AAAA): ").strip()

sexo = input("Sexo (H/M): ").strip().upper()
clave_estado = input("Escribe la clave de tu entidad (dos letras): ").strip().upper()

if len(dia) == 1:
    dia = "0" + dia

if len(mes) == 1:
    mes = "0" + mes

if len(anio) == 4:
    anio = anio[2:4]

if materno == "X":
    materno = ""

nombres = nombre.split()
paterno = paterno.split()[0] if paterno else ""
materno = materno.split()[0] if materno else ""

if nombres and nombres[0] in ("JOSE", "MARIA") and len(nombres) > 1:
    nombre_curp = nombres[1]
elif nombres:
    nombre_curp = nombres[0]
else:
    nombre_curp = ""

vocal = "X"
for letra in paterno[1:]:
    if letra in "AEIOU":
        vocal = letra
        break

inicial_materno = materno[0] if materno else "X"

consonante_paterno = "X"
for letra in paterno[1:]:
    if letra in "BCDFGHJKLMNPQRSTVWXYZ":
        consonante_paterno = letra
        break

consonante_materno = "X"
for letra in materno[1:]:
    if letra in "BCDFGHJKLMNPQRSTVWXYZ":
        consonante_materno = letra
        break

consonante_nombre = "X"
for letra in nombre_curp[1:]:
    if letra in "BCDFGHJKLMNPQRSTVWXYZ":
        consonante_nombre = letra
        break

if paterno and nombre_curp and len(dia) == 2 and len(mes) == 2 and len(anio) == 2 and sexo in ("H", "M") and clave_estado in estados.values():
    curp = (
        paterno[0] + vocal + inicial_materno + nombre_curp[0]
        + anio + mes + dia + sexo + clave_estado
        + consonante_paterno + consonante_materno + consonante_nombre
    )

    print("\nCurp:", curp[:16])
else:
    print("\nError: revisa tus datos y la clave de tu entidad.")
