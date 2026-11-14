nombre1 = input("¿Cual es tu primer nombre?")
nombre2 = input("¿Cual es tu segundo nombre?")
apellido1 = input("¿Cual es tu primer apellido")
apellido2= input("¿Cual es tu segundo apellido")

if nombre1=="" and apellido1=="":
    print("ERROR: NO PUEDES DEJAR EL PRIMER NOMBRE Y/O EL PRIMER APELLIDO VACIO")

if not(nombre1=="" and apellido1==""):
    if apellido2=="":
        apellido2="x"
    Curp= apellido1[0:2]+apellido2[0]+nombre1[0]
    print(Curp)