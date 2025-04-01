# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# edad_usuario = int(input("Ingrese su edad: "))

# if edad_usuario > 18:
#     print("Es mayor de edad")
    
# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

# nota = int(input("Ingrese su nota: "))

# if nota >= 6:
#     print("Aprobado")
# else:
#     print("Desaprobado6")
    
# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# numero_usuario = int(input("Ingrese un número: "))

# if numero_usuario % 2 == 0:
#     print("Ha ingresado un número par")
# else:
#     print("Por favor, ingrese un número par")
    
    
# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# edad_usuario = int(input("Ingrese su edad: "))

# if edad_usuario < 12:
#     print("Ustede pertenece a la categoría NIño/a")
# elif edad_usuario >= 12 and edad_usuario < 18:
#     print("Ustede pertenece a la categoría Adolescente")
# elif edad_usuario >= 18 and edad_usuario < 30:
#     print("Ustede pertenece a la categoría Adulto/a Joven")
# else:
#     print("Ustede pertenece a la categoría Adulto")
    

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# contrasegna = input("Ingrese su contraseña: ")

# if len(contrasegna) >= 8 and len(contrasegna) <= 14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
    
# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

# from statistics import mode, median, mean
# import random

# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# print(numeros_aleatorios)

# if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
#     print("Exite sesgo positivo en este grupo de números")
# elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
#     print("Exite sesgo negativo en este grupo de números")
# else:
#     print("No exite sesgo en este grupo de números")
    

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# frase_usuario = input("Ingrese una palabra o frase: ")

# ultimo_caracter = frase_usuario[-1]

# if ultimo_caracter == "a" or ultimo_caracter == "A" or frase_usuario == "e" or frase_usuario == "E" or frase_usuario == "i" or frase_usuario == "I" or frase_usuario == "o" or frase_usuario == "O" or frase_usuario == "u" or frase_usuario == "U":
#     frase_final = frase_usuario + "!"
#     print(frase_final)
# else:
#     print(frase_usuario)
    

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# nombre = input("Ingrese su nombre: ")
# opcion = input("Ingrese una opcion. 1) Su nombre en mayyuscular. 2) Su nombre en minúsculas. 3) Su nombre comn la primera letra mayúscula.")

# if opcion == "1":
#     print(nombre.upper())
# elif opcion == "2":
#     print(nombre.lower())
# elif opcion == "3":
#     print(nombre.title())
# else:
#     print("No es una opcion correcta")
    
    
# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# magnitud_terremoto = float(input("Ingrese la magnitud del terremoto a medir: "))

# if magnitud_terremoto < 3:
#     print("El terremoto es de categoría Muy Leve")
# elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
#     print("El terremoto es de categoría Leve")
# elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
#     print("El terremoto es de categoría Moderado")
# elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
#     print("El terremoto es de categoría Fuerte")
# elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
#     print("El terremoto es de categoría Muy Fuerte")
# elif magnitud_terremoto >= 7 and magnitud_terremoto <= 10:
#     print("El terremoto es de categoría Extremo")
# else:
#     print("Ingresó una categoría incorrecta. Debe estar entre 1 y 10")
    
    
# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Periodo del año
# Estación en el
# hemisferio norte
# Estación en el
# hemisferio sur
# Desde el 21 de diciembre hasta el 20 de
# marzo (incluidos)
# Invierno Verano
# Desde el 21 de marzo hasta el 20 de junio
# (incluidos)
# Primavera Otoño
# Desde el 21 de junio hasta el 20 de
# septiembre (incluidos)
# Verano Invierno
# Desde el 21 de septiembre hasta el 20 de
# diciembre (incluidos)
# Otoño Primavera
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese si está en el hemisferio norte(N) o en el hemisferio sur(S): ")
mes = int(input("Ingrese el mes del año en número: "))
dia = int(input("Ingrese el día del mes: "))

if dia >= 21:
    if mes == 12:
        if hemisferio == "N":
            print("Corresponde a invierno")
        elif hemisferio == "S":
            print("Corresponde a verano")
    elif mes == 3:
        if hemisferio == "N":
            print("Corresponde a primavera")
        elif hemisferio == "S":
            print("Corresponde a otoño")
    elif mes == 6:
        if hemisferio == "N":
            print("Corresponde a verano")
        elif hemisferio == "S":
            print("Corresponde a invierno")
    elif mes == 9:
        if hemisferio == "N":
            print("Corresponde a otoño")
        elif hemisferio == "S":
            print("Corresponde a primavera")
    elif mes == 1 or mes == 2:
        if hemisferio == "N":
            print("Corresponde a invierno")
        elif hemisferio == "S":
            print("Corresponde a verano")
    elif mes == 4 or mes == 5:
        if hemisferio == "N":
            print("Corresponde a primavera")
        elif hemisferio == "S":
            print("Corresponde a otoño")
    elif mes == 7 or mes == 8:
        if hemisferio == "N":
            print("Corresponde a invierno")
        elif hemisferio == "S":
            print("Corresponde a verano")
    elif mes == 10 or mes == 11:
        if hemisferio == "N":
            print("Corresponde a otoño")
        elif hemisferio == "S":
            print("Corresponde a primavera")
    else:
        print("No eligió una opción de mes válida")
elif dia < 21:
    if mes == 1 or mes == 2:
        if hemisferio == "N":
            print("Corresponde a invierno")
        elif hemisferio == "S":
            print("Corresponde a verano")
    elif mes == 3:
        if hemisferio == "N":
            print("Corresponde a invierno")
        elif hemisferio == "S":
            print("Corresponde a verano")
    elif mes == 4 or mes == 5:
        if hemisferio == "N":
            print("Corresponde a primavera")
        elif hemisferio == "S":
            print("Corresponde a otoño")
    elif mes == 6:
        if hemisferio == "N":
            print("Corresponde a primavera")
        elif hemisferio == "S":
            print("Corresponde a otoño")
    elif mes == 7 or mes == 8:
        if hemisferio == "N":
            print("Corresponde a invierno")
        elif hemisferio == "S":
            print("Corresponde a verano")
    elif mes == 9:
        if hemisferio == "N":
            print("Corresponde a verano")
        elif hemisferio == "S":
            print("Corresponde a invierno")
    elif mes == 10 or mes == 11:
        if hemisferio == "N":
            print("Corresponde a otoño")
        elif hemisferio == "S":
            print("Corresponde a primavera")
    elif mes == 12:
        if hemisferio == "N":
            print("Corresponde a otoño")
        elif hemisferio == "S":
            print("Corresponde a primavera")
    else:
        print("No eligió una opción de mes válida")
else:
    print("No eligió un día válido")