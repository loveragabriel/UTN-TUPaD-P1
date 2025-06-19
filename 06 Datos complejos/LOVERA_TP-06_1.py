'''
Estructura de Datos Complejas
Gabriel Lovera
'''
'''

####################################Actividades#################################33
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
'''
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
print(f"Listado de Frutas: {precios_frutas}")
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(f"Listado de Frutas actualizadas: {precios_frutas}")

'''
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(F"Precio de Frutas actualizados: {precios_frutas}")
'''
'''
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
listado_de_frutas = precios_frutas.keys()
print(listado_de_frutas)
'''
'''
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.


diccionario_telefonico = {}

for i in range(5):
    nombre = input("Ingrese un Nombre: ")
    numero = input("Indique ahora un numero: ")
    diccionario_telefonico[nombre]= numero

def preguntar_nombre(nombre, diccionario):
    if nombre in diccionario:
        print(f"El numero para {nombre} es {diccionario[nombre]}")
    else: print(f"No hay registro para el nombre {nombre}")

nombre = input("Ingrese un nombre para buscar su numero ")
preguntar_nombre(nombre, diccionario_telefonico)

5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
diccionario_frase = frase.split()
palabras_unicas = set(diccionario_frase)
print(f"Estas son las palabras únicas: {palabras_unicas}")
print("Repeticiones de cada palabra:")
    
contador_palabras= {}
for palabra in palabras_unicas:
    cantidad = diccionario_frase.count(palabra)
    contador_palabras[palabra] = cantidad
print(contador_palabras)

6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.


diccionario_alumnos = {}

for i in range(3):
    nombre_alumno = input("Ingrese nombre del alumno: ")
    notas_alumon = []
    for n in range(3):
        nota = float(input(f"Nota {n+1} para {nombre_alumno}: "))
        notas_alumon.append(nota)
    diccionario_alumnos[nombre_alumno] = tuple(notas_alumon)

print(diccionario_alumnos)

7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


parcial_1 = {("Ana", 8), ("Luis", 5), ("Juan", 9)}
parcial_2 = {("Ana", 7), ("Luis", 6), ("Marta", 10)}

aprobados_1={} 
for nombre, nota in parcial_1:
    if nota >= 6:
        aprobados_1[nombre] = nota

aprobados_2 = {}
for nombre, nota in parcial_2:
    if nota >= 6:
        aprobados_2[nombre] = nota

aprobados_ambos_parciales = set(aprobados_1) & set(aprobados_2)
aprobado_solo_1 = solo_uno = set(aprobados_1) ^ set(aprobados_2)
aprobados_al_menos_1 = al_menos_uno = set(aprobados_1) | set(aprobados_2)

print(f"Aprobaron ambos: {aprobados_ambos_parciales}")
print(f"Aprobaron solo uno: {aprobado_solo_1}")
print(f"Aprobaron al menos uno: {aprobados_al_menos_1}")


8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
'''

stock_productos = {
    "pan": 20,
    "leche": 6,
    "huevos": 20, 
    "azucar": 6
}

productos_ingresado = stock_productos.keys()
print(f"El esto de productos es {productos_ingresado}")

producto_agregar = input("Indique un productos para agregar unidades ").lower()

if producto_agregar in stock_productos:
    cantidad = int(input("¿Cuántas unidades querés agregar?: "))
    stock_productos[producto_agregar] += cantidad
    print(f"Nuevo stock de '{producto_agregar}': {stock_productos[producto_agregar]} unidades.")
else:
    print(f"El producto '{producto_agregar}' no existe en el stock, pero puede ingresarlo.")
    cantidad = int(input("¿Cuántas unidades tiene el nuevo producto?: "))
    stock_productos[producto_agregar] = cantidad
    print(f"Producto '{producto_agregar}' agregado con {cantidad} unidades.")
