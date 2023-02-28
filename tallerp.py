# Solicitar dos números al usuario
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

# Calcular el cociente y residuo de la división
cociente = n1 / n2
residuo = n1 % n2

# Mostrar el resultado al usuario
print("El cociente de la división entre", n1, "y", n2, "es:", cociente)
print("El residuo de la división", residuo)



altura_cm = float(input("Ingrese su altura en cm: "))  # Pedir al usuario la altura en cm
peso_kg = float(input("Ingrese su peso en kg: "))  # Pedir al usuario el peso en kg

# Convertir la altura a metros y calcular el IMC
altura_m = altura_cm / 100
imc =round( peso_kg / altura_m**2,2)

# Imprimir el resultado redondeado con dos decimales
print("Su IMC es ", imc)








precio_final = float(input("Ingrese el precio final del artículo o producto: "))

valor_iva = precio_final * 0.19 # Suponiendo un IVA del 19%
valor_bruto = precio_final - valor_iva

print("Valor del IVA: $", valor_iva)
print("Valor bruto del artículo o producto: $", valor_bruto)





# Solicitamos al usuario los datos necesarios
distancia_anual = float(input("Ingrese la distancia recorrida anual en kilómetros: "))
consumo_anual = float(input("Ingrese el consumo de combustible anual en litros cada 100 kilómetros: "))
costo_combustible = float(input("Ingrese el costo promedio anual del combustible por litro recorrido: "))

# Calculamos el costo anual del consumo de combustible
litros_anuales = consumo_anual * distancia_anual / 100
costo_anual = litros_anuales * costo_combustible

# Imprimimos el resultado en pantalla
print("El costo anual del consumo de combustible es de $", costo_anual)