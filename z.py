mes = int(input("Dime el mes al que quieres saber cuántos días tiene: "))
año = int(input("Dime el año a usar: "))

if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print("El año", año, "es bisiesto")

    match mes:
        case 1:
            print("Enero tiene 31 días")
        case 2:
            print("Febrero tiene 29 días")
        case 3:
            print("Marzo tiene 31 días")
        case 4:
            print("Abril tiene 30 días")
        case 5:
            print("Mayo tiene 31 días")
        case 6:
            print("Junio tiene 30 días")
        case 7:
            print("Julio tiene 31 días")
        case 8:
            print("Agosto tiene 31 días")
        case 9:
            print("Septiembre tiene 30 días")
        case 10:
            print("Octubre tiene 31 días")
        case 11:
            print("Noviembre tiene 30 días")
        case 12:
            print("Diciembre tiene 31 días")
        case _:
            print("Error: el mes debe estar entre 1 y 12")

else:
    print("El año", año, "no es bisiesto")

    match mes:
        case 1:
            print("Enero tiene 31 días")
        case 2:
            print("Febrero tiene 28 días")
        case 3:
            print("Marzo tiene 31 días")
        case 4:
            print("Abril tiene 30 días")
        case 5:
            print("Mayo tiene 31 días")
        case 6:
            print("Junio tiene 30 días")
        case 7:
            print("Julio tiene 31 días")
        case 8:
            print("Agosto tiene 31 días")
        case 9:
            print("Septiembre tiene 30 días")
        case 10:
            print("Octubre tiene 31 días")
        case 11:
            print("Noviembre tiene 30 días")
        case 12:
            print("Diciembre tiene 31 días")
        case _:
            print("Error: el mes debe estar entre 1 y 12")