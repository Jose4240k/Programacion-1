numero= int(input("Dame el numero a desglosar"))
millar= numero//1000
resto=numero%1000
centena=resto//100
resto=resto%100
Decena=resto//10
resto=resto%10
unidad= resto


print(f"El numero {numero}, tiene {millar} millares, {centena} centenas, {Decena} decenas y {unidad} unidades")