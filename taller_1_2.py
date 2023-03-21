#Taller_1 (segundo corte)
#Primer punto
import random

def aleatorio():
    num = random.randint(100, 120)
    while num in [110, 115, 119]:
        num = random.randint(100, 120)
    return num

for i in range(1, 11):
    num = aleatorio()
    if i % 2 == 0:
        print("Número par:", num)
    else:
        print("Número impar:", num)

#Segundo punto

import math as m

def calc(funcion, valor):
    if funcion == "seno":
        resultado = m.sin(valor)
    elif funcion == "coseno":
        resultado = m.cos(valor)
    elif funcion == "tangente":
        resultado = m.tan(valor)
    elif funcion == "exponencial":
        resultado = m.exp(valor)
    elif funcion == "logaritmo":
        resultado = m.log(valor)
    else:
        resultado = "Función no válida"
    return resultado

funcion = input("Ingrese la función a aplicar (seno, coseno, tangente, exponencial, logaritmo): ")
valor = float(input("Ingrese el valor: "))

resultado = calc(funcion, valor)
print(f"El resultado de la función {funcion} aplicada al valor {valor} es: {resultado}")





