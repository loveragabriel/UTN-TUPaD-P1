# TP-5 Funciones en Python
# Gabriel Lovera

# ACTIVIDADES

'''
ACT 1
Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
'''
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()   

'''
ACT 2
Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
'''
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
saludar_usuario("Gabriel")

'''
ACT 3 
Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
'''
def informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
informacion_personal("Gabriel", "Lovera","31", "CABA")


'''
ACT 4 
Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultad
'''
radio = float(input("Ingrese el Radio "))
def calcular_area_circulo(radio):
    area = float(3.1416 * (radio*radio))
    return area

def calcular_perimetro_circulo(radio):
    perimetro = float(2*3.1416*radio)
    return perimetro

print(f"El area de un círculo es {calcular_area_circulo(radio)} y el perimetro es {calcular_perimetro_circulo(radio)}")

'''
ACT 5
Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
'''
segundos = float(input("Ingrese segundos "))
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas
print(f"Los segundos ingresados corresponden a {segundos_a_horas(segundos)} Horas")

'''
ACT 6
Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
'''
numero = int(input("Ingrese un número para calcular su Tabla de Multiplicar "))
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {i*numero}")

tabla_multiplicar(numero)

'''
ACT 7
Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, 
multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
'''
a = 10
b = 6
def operaciones_basicas(a,b):
    suma = a + b
    resta = a -b
    multiplicacion = a *b
    division = a / b
    tupla=(suma,resta,multiplicacion,division)
    return tupla

resultados = operaciones_basicas(10,6)
print(f"La suma de {a} + {b} es : {resultados[0]}")
print(f"La resta de {a} - {b} es : {resultados[1]}")
print(f"La multiplicacion de {a} * {b} es : {resultados[2]}")
print(f"La division de {a} / {b} es : {resultados[3]}")

'''
ACT 8
Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales
'''
peso = float(input("Ingrese su peso "))
altura = float(input("Ingrese su altura en Metros "))
def calcular_imc(peso, altura):
    imc = peso/(altura**2 )
    print(f"Tu IMC es de {imc}")
calcular_imc(peso,altura)

'''
ACT 9
Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función
'''
celsius = float(input("Ingrese la temperatura el Celsius"))
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius*(9/5)) + 32
    return fahrenheit

resultado_conversion = celsius_a_fahrenheit(celsius)
print(f"La temperatura en grados {celsius} es {resultado_conversion} grados")


'''
ACT 10 
Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
'''
primer_numero = float(input("Ingrese el primer número "))
segundo_numero = float(input("Ingrese el segundo número "))
tercer_numero = float(input("Ingrese el Tercer número "))

def calcular_promedio(a, b, c):
    promedio = (a+b+c)/3
    return promedio

resultado_promedio =  calcular_promedio(primer_numero, segundo_numero, tercer_numero)
print(f"El promedio de {primer_numero}, {segundo_numero}, {tercer_numero} es: {resultado_promedio}")