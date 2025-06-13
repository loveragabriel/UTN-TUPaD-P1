''' TP RECURSIVIDAD '''

'''
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
'''
def funcion_factorial(num):
    #Caso Base
    if num== 0: 
        return 1
    # Aplicación de caso de recursividad
    else:
        return num * funcion_factorial(num-1)

numero = int(input("Ingrese un número para evaluar su factorial: "))
print(f"Factoriales del 1 al {numero}:")

#Iteramos la presentación de cada llamada recursiva. 
for i in range(1, numero + 1):
    print(f"El factorarial de {i} es = {funcion_factorial(i)}")

'''    
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
'''
def fibonacci(n):
    #Caso basse
    if n == 0:
        return 0
    #caso base
    elif n == 1:
        return 1
    #Recursividad de la función que calcula una serie Fibonacci 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Solicitud de Posición
posicion = int(input("Ingrese hasta qué posición desea ver la serie de Fibonacci: "))

# Se imprime resultado. 
print(f"Serie de Fibonacci hasta la posición {posicion}:")
for numero  in range(posicion + 1):
    print(f"Posición {numero}  = {fibonacci(numero)}")

'''    
3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula n'𝑚 = n * n'(𝑚-1)
Prueba esta función en un algoritmo general.
'''
def calcular_potencia(base, ptencia):
    #Caso base
    if ptencia == 0:
        return 1
    # Aplicación de recursividad para calcular la potencia, 
    else:
        return base * calcular_potencia(base, ptencia - 1)

# Se solicitan base y exponente. 
base = int(input("Ingrese la base: "))
ptencia = int(input("Ingrese la potencia: "))

#Se imprime resultado
print(f" El número {base} elevado a la {ptencia} es igual a {calcular_potencia(base, ptencia)}")

'''
4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
'''
def decimal_a_binario(num):
    #Caso base
    if num == 0:
        return ""
    #Parte de recursividad 
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

# SOlicitda numero decima
numero = int(input("Ingrese un número entero positivo: "))

# Se imprime excepción. 
if numero == 0:
    print("El número 0 es igual a 0 en binaro.")
# Impresión de numero bianrio. 
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")

'''
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
 Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
'''
def evaluar_palabra(palabra):
    # Se evalua caso base 
    if len(palabra) <= 1:
        return True
    # Se evaluan excepciones que son palindromos 
    if palabra[0] != palabra[-1]:
        return False
    # Se aplica recursividad utilizando listas para evaluar los caracteres desde el ultimo al primero
    return evaluar_palabra(palabra[1:-1])

# Se estanadariza la palabra a minusculas
texto = input(f"Ingrese una palabra sin espacios:").lower()

# Evaluamos condición de es True impre que es palindromo 
if evaluar_palabra(texto):
    print(f' La palabra "{texto}" es un palíndromo.')
# Se imprime caso negativo.
else:
    print(f'"{texto}" no es un palíndromo.')
    
'''
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
'''
def suma_digitos(numero):
    #Establezco caso base
    if  numero < 10:
        return numero
    #Aplico recursividad, reduciendo el decimal y volviendo a llamar la función
    else: return numero % 10 + suma_digitos(numero // 10)

# Ejemplo 1
print(f"Ejemplo 1: {suma_digitos(15963)}")
# Ejemplo 2
print(f"Ejemplo 2 : {suma_digitos(8)}")
# Ejemplo 3
print(f"Ejemplo 3 : {suma_digitos(2000001)}")
'''
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)
'''
def contar_bloques(n):
    # Caso base
    if n < 1:
        return n
    # Se aplica recursividad. 
    else: return n + contar_bloques(n-1)

# Ejemplo 1
print(f"Ejemplo num 3: {contar_bloques(3)}")
# Ejemplo 2
print(f"Ejemplo num 4 : {contar_bloques(4)}")
# Ejemplo 3
print(f"Ejemplo num 15 : {contar_bloques(15)}")

'''
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0
'''
def conatr_digito(numero, digito):
    #Caso base
    if numero == 0:
        return numero
    # Aplicación de recursividad
    else: 
        # Se va reduciendo el número por decenas
        ultimo_digito = numero % 10
        # Se evalua si el ultimo numero evaluado es igual al digito ingresado
        if ultimo_digito == digito:
            # Si coincide suma 1 y continua con la recursividad
            return 1 + conatr_digito(numero//10, digito)
        # Si el ultimo numero no es igual se continua la recursividad pero no hay suma 
        else: return conatr_digito(numero // 10, digito)

#Se imprimen ejemplos. 
print(f"El digito ingresado de repite {conatr_digito(95809457,5)} veces!")
print(f"El digito ingresado de repite {conatr_digito(95809457,2)} veces!")