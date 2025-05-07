# Práctico 4: Estructuras repetitivas
# Gabriel Lovera

################
##Actividades##
################


#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

###############################################################################################
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
numero = int(input("Ingrese un número entero"))

count = 0
while numero > 0:
    numero //= 10
    count += 1

print(f"El número tiene {count} digitos")
    
###############################################################################################
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#   dados por el usuario, excluyendo esos dos valores.

numero_1 = int(input("Ingrese primer número"))
numero_2 = int(input("Ingrese segundo número"))

sumatoria = 0

if numero_1 < numero_2:
    for i in range(numero_1+1, numero_2):
        sumatoria += i
elif numero_1 > numero_2:
    for i in range(numero_2+1, numero_1):
        sumatoria += i

print(f"La suma total es {sumatoria}")

###############################################################################################
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0 

sumatoria = 0
while True:
    valor = int(input("Ingrese un numero para sumar y 0 para detener"))
    if valor == 0:
        break    
    sumatoria += valor

print(f"La suma de los número ingresados es de {sumatoria}")

###############################################################################################
#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

numero = int(input("Adivina el número entre el 0 y 9"))
numero_aleatorio = random.randint(0, 9)

while numero < 0 or numero > 9:
    numero = int(input("Adivina el número entre el 0 y 9"))
intentos = 1
while numero_aleatorio != numero:
        numero = int(input("Adivina el número entre el 0 y 9"))
        intentos += 1

print(f"El numero es correcto y tus intentos fueron de {intentos} veces")

###############################################################################################
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#   entre 0 y 100, en orden decreciente.

for i in range(100,-1,-1):
    if i %2 ==0:
        print(i)

###############################################################################################
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero_positivo = int(input("Ingrese un numero mayor a 0"))

sumatoria_positivo = 0
for i in range(numero_positivo+1):
    sumatoria_positivo += i
print(f"La sumatoria de los valores entre 0 y tu número es de {sumatoria_positivo}")

###############################################################################################
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).


numeros_pares = 0
numeros_impares = 0
numeros_negativos = 0
numeros_positivo = 0
contador = 100

for  i in range(100):
    numeros_ingresados = int(input(f"Ingrese 100 numeros; quedan {contador-i}"))
    if numeros_ingresados > 0:
        numeros_positivo += 1
        if numeros_ingresados % 2==0:
            numeros_pares += 1
        else:
            numeros_impares +=1
    elif numeros_ingresados < 0:
        numeros_negativos += 1
        if numeros_ingresados % 2==0:
            numeros_pares += 1
        else:
            numeros_impares +=1
    contador -= 1

print(f"Ingresaste {numeros_positivo} numeros positivos")
print(f"Ingresaste {numeros_negativos} numeros negativos")
print(f"Ingresasre {numeros_pares} números pares")
print(f"Ingresaste {numeros_impares} núemros impares")


###############################################################################################
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

sumatoria_media = 0
for i in range(100):
    numeros_a_evaluar = int(input(F"Ingrese el número {i + 1} de 100 para calcular la media:"))
    sumatoria_media += numeros_a_evaluar

media = sumatoria_media/100

print(f"La media de los números ingresados es de {media}")

###############################################################################################
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero_a_invertir = int(input(f"Ingrese un número para invertir sus digitos"))

numero_invertido = 0
negativo = False

if numero_a_invertir < 0 :  
     numero_a_invertir = numero_a_invertir *-1
     negativo = True

while numero_a_invertir > 0:
    digito_final =  numero_a_invertir % 10

    numero_invertido = numero_invertido * 10 + digito_final
    numero_a_invertir = numero_a_invertir  // 10

if negativo:
    print(f"Su numero invertifo es -{numero_invertido}")
else:
        print(f"Su numero invertifo es {numero_invertido}")






