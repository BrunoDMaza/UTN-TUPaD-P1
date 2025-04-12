# ========== Ejercicio 1 ==========

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for i in range (101):
#     print(i)

# ========== Ejercicio 2 ==========
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# numero = input("Ingrese un número: ")
# cant_digitos = len(numero)

# print(f"La cantidad de dígitos que tiene {numero} es de {cant_digitos}")

# ========== Ejercicio 3 ==========
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# numero1 = int(input("Ingrese el primer número: "))
# numero2 = int(input("Ingrese el segundo número: "))

# suma = 0

# for i in range(numero1 + 1, numero2):
#     suma += i
    
# print(f"La suma de los números comprendidos entre {numero1} y {numero2} es {suma}")

# ========== Ejercicio 4 ==========
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# numero = 1

# suma = 0
# while numero != 0:
#     numero = int(input("Ingrese un número entero: "))
#     suma += numero


# print(f"La suma de los números ingresados es {suma}")

# ========== Ejercicio 5 ==========
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#importo para lograr generar números al azar
# import random 

# sigue = "s"

# coincidencias = 0

# while sigue != "n" and sigue != "N":
#     numero = int(input("Ingrese un número entero: "))
#     numero_azar = random.randint(0, 9)
#     print(f"El numero ingresado es {numero} y el número al azar es {numero_azar}")
#     if numero == numero_azar:
#         coincidencias += 1
#     sigue = input("¿Quiere seguir adiviando? Escriba n para dejar de jugar: ")
    


# print(f"La cantidad de coincidencias es {coincidencias}")

# ========== Ejercicio 6 ==========
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# for i in range(100, 0, -2):
#     print(i)


# ========== Ejercicio 7 ==========
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario

# numero = int(input("Ingrese un número entero positivo: "))
# suma = 0
# if numero > 0:
#     for i in range(0, numero + 1):
#         suma += i
# else:
#     print("No ingresó un número positivo")
    
# print(f"La suma de los números entre 0 y {numero} es {suma}")

# ========== Ejercicio 8 ==========
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# cant_veces = 10
# num_pares = 0
# num_impares = 0
# num_positivos = 0
# num_negativos = 0

# for i in range(0, cant_veces):
#     numero = int(input(f"Ingrese el número numero {i + 1}: "))
#     if numero >= 0:
#         num_positivos +=1
#     else:
#         num_negativos += 1
#     if numero % 2 == 0:
#         num_pares += 1
#     else:
#         num_impares += 1
        
# print(f"Los número positivos fueron {num_positivos}, los número negativos fueron {num_negativos}, los pares fueron {num_pares} y los impares fueron {num_impares}")


# ========== Ejercicio 9 ==========
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# cant_veces = 10
# suma = 0

# for i in range(0, cant_veces):
#     numero = int(input(f"Ingrese el número numero {i + 1}: "))
#     suma += numero
        
# print(f"La media de los números ingresados es {suma/cant_veces}")


# ========== Ejercicio 10 ==========
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

cadena = input("Ingrese una cifra: ")
nueva_cifra = ""

for i in range(len(cadena) - 1, -1, -1):
    nueva_cifra += cadena[i]
    

print(f"La cifra {cadena} al revés es {nueva_cifra}")