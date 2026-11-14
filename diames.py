import primo as pe

a=int(input("Dame el año"))
m=int(input("Dame el mes en un rango de 1 a 12"))
d=int(input("Dame el dia del mes"))

res=pe.diames(a,m,d)

print(res)