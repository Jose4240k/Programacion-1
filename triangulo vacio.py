n= int(input("n="))
for i in range(1,n+1):
    espacios= " " * (n-i)
    if i ==1:
        print(espacios +"*")
    elif i==n:
        print("*"*(2*i-1))
    else:
        print(espacios+"*"+" "*(2*i-3)+"*")
    
