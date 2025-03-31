# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

# Brrun

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

# nombre = input("Ingrese su nombre")

# print(f"Hola {nombre}")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla

# nombre = input("Ingrese su nombre ")
# apellido = input("Ingrese su apellido ")
# edad = input("Ingrese su edad")
# lugar_residencia = input("Ingrese su lugar de residencia ")

# print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro

# radio = int(input("Ingrese el radio del circulo a calcular"))

# area = 3.14*(radio**2)
# perimetro= 2*3.14*radio
# print(f"Un circulo con un radio de {radio} posee un area de {area} y un perímetro de {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

# segundos = int(input("Ingrese la cantidad de segundo para calcular la cantidad de horas "))
# horas = segundos / 3600

# print(f"Para {segundos} cantidad de segundo tenemos {horas:.4f} cantidad de horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

# numero = int(input("Ingrese un número"))

# for i in range (1,11):
#     resultado = numero*i
#     print(f"{numero} X {i} = {resultado}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

# numero1 = int(input("IUngrese el primer número distinto a 0"))
# numero2 = int(input("IUngrese el segundo número distinto a 0"))

# suma = numero1 + numero2
# resta = numero1 - numero2
# multiplicacion = numero1 * numero2
# division = numero1 / numero2

# print(f"El resultadod de la suma de {numero1} y {numero2} es {suma}")
# print(f"El resultadod de la resta de {numero1} y {numero2} es {resta}")
# print(f"El resultadod de la multiplicación de {numero1} y {numero2} es {multiplicacion}")
# print(f"El resultadod de la division de {numero1} y {numero2} es {division}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.

# peso = float(input("Ingrese su peso: "))
# altura = float(input("Ingrese su altura: "))

# masa_corporal = peso / (altura)**2
# print(f"El índice de masa corporal con {peso} kgs de peso y con una altura de {altura} es de {masa_corporal:.2f}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.

# temperatura_en_c = float(input("Ingrese la temperatura en grados celsius: "))
# temperatura_en_f = (9/5) * temperatura_en_c + 32

# print(f"{temperatura_en_c} grados Celsius son {temperatura_en_f} grados Fahrenheit")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de {numero1}, {numero2} y {numero3} es {promedio}")