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
numero = 1

suma = 0
while numero != 0:
    numero = int(input("Ingrese un número entero: "))
    suma += numero


print(f"La suma de los números ingresados es {suma}")

# ========== Ejercicio 5 ==========
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# ========== Ejercicio 6 ==========
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# ========== Ejercicio 7 ==========
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario

# ========== Ejercicio 8 ==========
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# ========== Ejercicio 9 ==========
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# ========== Ejercicio 10 ==========
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

