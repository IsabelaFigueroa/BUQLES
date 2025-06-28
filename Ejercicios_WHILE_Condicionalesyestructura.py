# #EJERCICIOS CON WHILE, CONDICIONALES Y ESTRUCTURAS
#1. Suma hasta cero
#Pide al usuario números enteros y súmalos hasta que ingrese un 0. Luego muestra el total
suma= 0
numero= int(input("Ingrese un numero entero (0 para terminar): "))
while numero !=0:
    suma+=numero
    numero=int(input("Ingrese otro numero entero (0 para terminar): "))
    print("La suma total es: ",suma)
#--------------------------------------------------------------------------------------------------------
#2. Contraseña secreta
#Crea un programa que pida una contraseña usando while hasta que escriba "python123" correctamente.
contraseña = input("Ingresar la contraseña: ")
while contraseña != "python123":
    print("Contraseña incorrecta")
    contraseña = input("Intenta de nuevo: ")
print("¡Puedes acceder!")
#--------------------------------------------------------------------------------------------------------
#3. Lista de compras
#Pide productos uno por uno y guárdalos en una lista. Termina cuando el usuario escriba
#"fin", luego muestra toda la lista.
productos=[ ]
producto=input("Ingrese un producto (escribe fin para terminar): ")
while producto != "fin":
    productos.append(producto)
    producto=input("Ingresa otro producto (escribe fin para terminar): ")
print("Lista de compras: ")
print(productos)
#-------------------------------------------------------------------------------------------------------
#4. Contador de pares e impares
#Pide 10 números al usuario. Usa while para contarlos y guarda cuántos son pares y cuántos impares.
pares= 0
impares= 0
contador= 0
while contador  < 10:
    contador=int(input("Ingrese un numero: "))
    if contador % 2 == 0:
        pares += 1
    else:
        impares += 1
    contador += 1

print(f"pares{pares}, impares{impares}")
#--------------------------------------------------------------------------------------------------------
#5. Promedio de calificaciones
#Pide al usuario ingresar notas entre 0 y 5 hasta que escriba "salir". Guarda las notas en
#una lista y muestra el promedio. 
notas = []
entrada = input("Ingresa una nota (0 a 5) o 'salir' para terminar: ")

while entrada != "salir":
    nota = float(entrada)
    if 0 <= nota <= 5:
        notas.append(nota)
    else:
        print("Nota inválida. Debe estar entre 0 y 5.")
    entrada = input("Ingresa otra nota (o 'salir' para terminar): ")

if notas:
    promedio = sum(notas) / len(notas)
    print("El promedio de las notas es:", promedio)
else:
    print("No se ingresaron notas válidas.")
#---------------------------------------------------------------------------------------------------------
#6. Tabla de multiplicar interactiva
#Pide un número y genera su tabla del 1 al 10 con while.
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
contador = 1

while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1
#-----------------------------------------------------------------------------------------------------
#7. Adivina el número
#El programa tiene un número secreto (ej. 17). El usuario tiene que adivinarlo. Con cada
#intento, el programa dice si es mayor o menor.
secreto= 16
intento=int(input("Adivina el numero: "))

while intento != secreto:
    if intento < secreto:
        print ("Es mayor")
    else: 
        print("Es menor")
    intento= int(input("Intenta otra vez: "))

print("¡Correcto! ¡Adivinaste el numero!")
------------------------------------------------------------------------------------------------------
#8. Tupla de frutas
#Crea una tupla con frutas. Usa while para pedirle al usuario que adivine frutas hasta que
#acierte una que esté en la tupla.
frutas=("manzana","fresa","cereza","mango","limon")
while True:
    adivina=input("Adivina la fruta: ").lower()
    if adivina in frutas:
        print("¡Correcto!Esa fruta esta en la lista")
        break
    else:
        print("Incorrecto.Intenta de nuevo")
#-------------------------------------------------------------------------------------------------------
#9. Diccionario de traducción
#Crea un diccionario con 5 palabras en español y su traducción al inglés. Usa while para
#que el usuario ingrese una palabra en español y muestre su traducción (si está).
diccionario = {
    "hola": "hello",
    "gracias": "thank you",
    "perro": "dog",
    "gato": "cat",
    "adios": "goodbye"
}

while True:
    palabra = input("Ingresa una palabra en español (o escribe 'salir'): ").lower()
    if palabra == "salir":
        break
    if palabra in diccionario:
        print(f"La traducción es: {diccionario[palabra]}")
    else:
        print("Palabra no encontrada.")
#----------------------------------------------------------------------------------------------------
#10. Calculadora básica
#Haz un menú dentro de un while para que el usuario elija:
#1. Sumar
#2. Restar
#3. Multiplicar
#4. Dividir
#5. Salir
#Luego realiza la operación con dos números ingresados.

while True:
    print("\nCalculadora:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("Saliendo...")
        break

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print(f"Resultado: {num1 + num2}")
    elif opcion == "2":
        print(f"Resultado: {num1 - num2}")
    elif opcion == "3":
        print(f"Resultado: {num1 * num2}")
    elif opcion == "4":
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("No se puede dividir por cero.")
    else:
        print("Opción no válida.")
 -------------------------------------------------------------------------------------------------
#11. Registro de edades
#Pide nombres y edades de personas y guárdalos en un diccionario. Detente cuando el
#usuario escriba "salir" como nombre. Luego muestra el diccionario completo.
edades = {}

while True:
    nombre = input("Ingresa un nombre (o escribe 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    edades[nombre] = edad

print("\nDiccionario de edades:")
print(edades)
#-----------------------------------------------------------------------------------------------------
#12. Buscar en lista
#Crea una lista de 5 colores. Usa un bucle while para que el usuario escriba colores hasta
#encontrar uno que esté en la lista.
colores = ["rojo", "azul", "verde", "amarillo", "morado"]

while True:
    color = input("Escribe un color: ").lower()
    if color in colores:
        print(f"¡Sí! {color} está en la lista.")
        break
    else:
        print("Ese color no está en la lista. Intenta otra vez.")
#---------------------------------------------------------------------------------------------------------
#13. Potencias de un número
#Pide un número y muestra sus potencias desde la 1 hasta la 5 con while.
numero = int(input("Ingresa un número: "))
potencia = 1

while potencia <= 5:
    resultado = numero ** potencia
    print(f"{numero} elevado a {potencia} es {resultado}")
    potencia += 1
#--------------------------------------------------------------------------------------------------------
#14. Lista de cuadrados
#Pide 5 números con while y guarda en una lista sus cuadrados. Al final, muestra la lista.
cuadrados = []
contador = 0

while contador < 5:
    num = int(input("Ingresa un número: "))
    cuadrados.append(num ** 2)
    contador += 1

print("Lista de cuadrados:", cuadrados)
#------------------------------------------------------------------------------------------------------
#15. Diccionario de estudiantes
#Crea un programa que te deje registrar estudiantes con su nota final (nombre y nota). Usa
#un diccionario. El usuario debe poder agregar varios hasta que escriba "fin".
estudiantes = {}

while True:
    nombre = input("Nombre del estudiante (o escribe 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    nota = float(input(f"Nota final de {nombre}: "))
    estudiantes[nombre] = nota

print("\nDiccionario de estudiantes:")
print(estudiantes)
#Trabajo terminado