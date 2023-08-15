precio= float (input("Introduce el precio: "))
mensaje = ""

if precio > 0 :
    print ("El precio es válido")
    mensaje="El precio es válido"
else :
    print ("El precio no es válido")
    mensaje="El precio no es válido"

print(mensaje)
#print(f"Precio: ${precio}")
