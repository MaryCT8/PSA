#string se usa para caracteres
#integer 321 (whole number)
#float 321.0 decimales
#boolean: true or false (binarios)
#a//b division con redondeo
#a % b modulo (residuo de la division entre a y b)
#a**b potencia
#pass para que el codigo no muestre error
#elif (condicionales)
#for es un bloque definido a comparacion de while
# para comentar en masa control + k  despues control + c para comentarlo y para descomentarlo control + u , otra
#manera de contar es con tres comillas al inicio y al final '''

#for + variable= rango i

print('escoja una de las siguientes opciones:\n1')
print('1. for in range(final)')
print('2. for in range(inicio,final)')
print('3. for in range(inicio, final, paso)')
opc=int(input('Escoja una opcion: '))
if opc ==1:
  for i in range(10):
    print(i+1)
  print('fin del proceso')

elif opc=='2':
  pass


#def se refiere a funcion
def suma(a,b):
  rsultado=a+b
  return resultado
print(suma(5,6))

def imprimir():
  print('su resultado es: ')

#res se usa para
n='si'
while n== 'si':
    a =int(input("ingresa un numero a "))
    b =int(input("ingresa un numero b "))
    res = suma (a,b)
    imprimir(nombre)
    print(res)
    n=input('Quiere sumar otro numero? (si/no): ')

#funcion que calcula el area de un circulo
