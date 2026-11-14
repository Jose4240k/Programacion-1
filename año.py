numero = int(input("Ingresa un número del 1 al 3999: "))

if numero < 1 or numero > 3999:
    print("Error: el número debe estar entre 1 y 3999.")
else:
    millares = numero // 1000
    centenas = (numero % 1000) // 100
    decenas = (numero % 100) // 10
    unidades = numero % 10

    romano = ""

    match millares:
        case 1:
            romano += "M"
        case 2:
            romano += "MM"
        case 3:
            romano += "MMM"

    match centenas:
        case 1:
            romano += "C"
        case 2:
            romano += "CC"
        case 3:
            romano += "CCC"
        case 4:
            romano += "CD"
        case 5:
            romano += "D"
        case 6:
            romano += "DC"
        case 7:
            romano += "DCC"
        case 8:
            romano += "DCCC"
        case 9:
            romano += "CM"

    match decenas:
        case 1:
            romano += "X"
        case 2:
            romano += "XX"
        case 3:
            romano += "XXX"
        case 4:
            romano += "XL"
        case 5:
            romano += "L"
        case 6:
            romano += "LX"
        case 7:
            romano += "LXX"
        case 8:
            romano += "LXXX"
        case 9:
            romano += "XC"

    match unidades:
        case 1:
            romano += "I"
        case 2:
            romano += "II"
        case 3:
            romano += "III"
        case 4:
            romano += "IV"
        case 5:
            romano += "V"
        case 6:
            romano += "VI"
        case 7:
            romano += "VII"
        case 8:
            romano += "VIII"
        case 9:
            romano += "IX"

    print("Número romano:", romano)