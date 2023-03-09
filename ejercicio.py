
def Area(r):
    pi=3.1416
    A=pi*(r**2)
    return A

def volumen(h,r):
    
    V=A*h
    return V

r=int(input("Ingresa el valor del radio"))
h=int(input("Ingresa el valor de la altura"))

A=Area(r)
V=volumen(h,A)

p3
rint(f'El area es {A} y el volumen es {V}')