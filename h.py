m=int(input("altura"))
for i in range(1,m+1):
    espacios=" " *(m-i)
    asteriscos="*" *(2*i-1)
    print(espacios + asteriscos)
for a in range(m-1,0,-1):
    espacios=" " *(m-a)
    asteriscos="*" *(2*a-1)
    print(espacios + asteriscos)