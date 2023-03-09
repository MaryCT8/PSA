print('escoja una de las siguientes opciones:\n1')
print('1. Programa que pide al usuario un numero entero positivo y despues imprima en pantalla todos los numeros impares desde el 1 hasta dicho numero separado por comas')
print('2. Programa que calcula el numero factorial de un numero ')
print('3. Programa que solicita un numero, despues indica si es primo o no; ademas imprime los numeros primos hasta ese numero')
opc=int(input('Escoja una opcion: '))
if opc ==1:
    n = int(input("ingrese un numero positivo mayor a cero "))
    impares = []
    if n <= 0:
        print("Ingrese de nuevo un numero, teniendo en cuenta que sea entero y mayor a 0")
    else:
        for i in range(1, n+1):
         if (i % 2) != 0:
            impares.append(str(i))
            impares_str = ", ".join(impares)

    print("Los números impares son: " + impares_str)

elif opc=='2':
    n = int(input("ingrese un numero positivo mayor a cero "))
    n_f = 1

    if n <= 0:
        print("Ingrese de nuevo un numero, teniendo en cuenta que sea entero y mayor a 0")
    else:
                for i in range(1, n+1):
                    n_f *= i

    print("El factorial de", n, "es", n_f)

elif opc=='3':
    n = int(input("Ingresa un número entero mayor que 1: "))
    if n > 1:
        for i in range(2, n+1):
            es_primo = True
            for j in range(2, i):
                if i % j == 0:
                    es_primo = False
                    break
            if es_primo:
                print(i, "es un número primo")
    else:
        print("El número debe ser mayor que 1")
