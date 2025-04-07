#Actividades PT_03

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#   deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”
print("Ejercicio 1")

edad = int(input("Ingrese su edad"))

if edad >= 18:
    print("Es mayor de edad")
pass

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#    mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#    mensaje “Desaprobado”

print("Ejercicio 2")

nota = float(input("Ingrese su nota"))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

print("Ejercicio 3")

numero_par = int(input("Ingrese un número"))

if numero_par % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
...
# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
#   ● Niño/a: menor de 12 años.
#   ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#   ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#   ● Adulto/a: mayor o igual que 30 años.

print("Ejercicio 4")

edad = int(input("Ingrese su edad"))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a Joven ")
elif edad >= 30:
    print("Adulto/a")
pass

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

print("Ejercicio 5")

contraseña = str(input("Ingrese una contraseña entre 8 y 14 caracteres"))
len_contraseña = len(contraseña)

if len_contraseña >= 8 and len_contraseña <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
pass


# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números.
from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

the_mode = float(mode(numeros_aleatorios)); 
the_median = float(median(numeros_aleatorios));
the_mean = float(mean(numeros_aleatorios));

if the_mean > the_median and the_median > the_mode:
    print("Sesgo Positivo o a la derecha")
elif the_mean < the_median and the_median < the_mode:
    print("Sesgo negativo o a la izquierda")
elif (the_mode == the_mean) and (the_mean == the_median):
    print("Sin Sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

print("Ejercicio 7")

word = str(input("Ingrese una frase o palabra"))

final_letter = word[-1]
letter = final_letter.upper()

if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
    print(word,"!")
else:
    print(word)

    
# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
#   1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#   2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#   3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

print("Ejercicio 8")

name = str(input("Ingrese su nombre"))
number = int(input("1. Si quiere su nombre en mayúsculas. Ejemplo: PEDRO\n" "2. Si quiere su nombre en minúsculas. Ejemplo: pedro\n" "3. Si quiere su nombre con la primera letra mayúscula. Ejemplo: Pedro\n"))

if number == 1:
    print(name.upper())
elif number == 2:
    print(name.lower())
elif number == 3:
    print(name.title())


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
#   ● Menor que 3: "Muy leve" (imperceptible).
#   ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#   ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#   ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#   ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#   ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

print("Ejercicio 9")

magnitud = float(input("Ingrese magnitud del terremoto"))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte")
elif magnitud >= 7:
    print("Extremo")
pass

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

print("Ejercicio 10")

hemisferio = str(input("Indique en qué Hemisferio se encuentra: \n N Para el Norte  \n S Para el Sur"))
mes_anio = str(input("Ingrese el mes de año, ejemplo: enero"))
dia = int(input("Ingrese el día, ejemplo 06"))

hemisferio_upper = hemisferio.upper()
mes_anio_upper = mes_anio.upper()
periodo_anio = 0

if mes_anio_upper == "DICIEMBRE":
    if dia >= 21:
        periodo_anio = 1
    else:
        periodo_anio = 4
elif mes_anio_upper == "ENERO" or mes_anio_upper == "FEBRERO":
    periodo_anio = 1
elif mes_anio_upper == "MARZO":
    if dia <=20:
        periodo_anio = 1
    else:
        periodo_anio = 2
elif mes_anio_upper == "ABRIL" or mes_anio_upper == "MAYO":
    periodo_anio = 2
elif mes_anio_upper == "JUNIO":
    if dia <= 20:
        periodo_anio = 2
    else:
        periodo_anio = 3
elif mes_anio_upper == "JULIO" or mes_anio_upper == "AGOSTO":
        periodo_anio = 3
elif mes_anio_upper == "SEPTIEMBRE":
    if dia <= 20:
        periodo_anio = 3
    else:
        periodo_anio = 4
elif mes_anio_upper == "OCTUBRE" or mes_anio_upper == "NOVIEMBRE":
    periodo_anio = 4
pass

if hemisferio_upper == "N":
    if periodo_anio == 1:
        print("Estacion Invierno")
    elif periodo_anio == 2:
        print("Estacion del año primavera")
    elif periodo_anio == 3:
        print("Estacion del año verano")
    else:
        print("Estacion del año Otoño")
elif hemisferio_upper == "S":
    if periodo_anio == 1:
        print("Estacion del año Verano")
    elif periodo_anio == 2:
        print("Estacion del año Otoño")
    elif periodo_anio == 3:
        print("Estacion del año Inverno")
    else:
        print("Estacion del año Primavera")