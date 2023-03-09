numb=int(input('Escribe un numero entre 2 y 8 digitos: '))

if numb<= 0:
        print("Ingrese de nuevo un numero, teniendo en cuenta que sea entero y mayor a 0")
else:
    numb>0
    resultado = numb//10
    resultado1 = resultado*10
    totaln= resultado - resultado1
    print("digito diferente de 5: ", totaln)

