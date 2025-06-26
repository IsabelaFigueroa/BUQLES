# #EJERCICIOS CON WHILE, CONDICIONALES Y ESTRUCTURAS
# #1. Suma hasta cero
# #Pide al usuario números enteros y súmalos hasta que ingrese un 0. Luego muestra el total
# suma= 0
# numero= int(input("Ingrese un numero entero (0 para terminar): "))
# while numero !=0:
#     suma+=numero
#     numero=int(input("Ingrese otro numero entero (0 para terminar): "))
#     print("La suma total es: ",suma)
# #--------------------------------------------------------------------------------------------------------
# #2. Contraseña secreta
# #Crea un programa que pida una contraseña usando while hasta que escriba "python123" correctamente.
# contraseña = input("Ingresar la contraseña: ")
# while contraseña != "python123":
#     print("Contraseña incorrecta")
#     contraseña = input("Intenta de nuevo: ")
# print("¡Puedes acceder!")
# #--------------------------------------------------------------------------------------------------------
# #3. Lista de compras
# #Pide productos uno por uno y guárdalos en una lista. Termina cuando el usuario escriba
# #"fin", luego muestra toda la lista.
# productos=[ ]
# producto=input("Ingrese un producto (escribe fin para terminar): ")
# while producto != "fin":
#     productos.append(producto)
#     producto=input("Ingresa otro producto (escribe fin para terminar): ")
# print("Lista de compras: ")
# print(productos)
# #-------------------------------------------------------------------------------------------------------
# #4. Contador de pares e impares
# #Pide 10 números al usuario. Usa while para contarlos y guarda cuántos son pares y cuántos impares.
# pares= 0
# impares= 0
# contador= 0
# while contador  < 10:
#     contador=int(input("Ingrese un numero: "))
#     if contador % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
#     contador += 1

# print(f"pares{pares}, impares{impares}")
#--------------------------------------------------------------------------------------------------------
#5. Promedio de calificaciones
#Pide al usuario ingresar notas entre 0 y 5 hasta que escriba "salir". Guarda las notas en
#una lista y muestra el promedio. 
notas= [ ]    
entrada=float(input("Ingresa una nota (0 a 5) o 'salir' para terminar: "))
while entrada=float(input("Ingresa una nota (0 a 5) o 'salir' para terminar: "))
entrada != "salir":  
nota= (entrada)
if 0 <= nota <=5:
        notas.append(nota)
else:
        print("Nota invalida debe ser entre 0 y 5")
entrada=input("Ingresa otra nota(o 'salir' para terminar): ")
if notas:
        promedio=sum(notas)/ len (notas)
        print("El promedio de las notas es: ",promedio)
else:
        print("No se ingresaron notas validas")

#CODIGO MAL


