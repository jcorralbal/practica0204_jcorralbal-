#Escribir un programa que pregunte por una muestra de números, separados por 
#comas, los guarde en una lista y muestre por pantalla su media y desviación
#típica.

lista = input("Introduce una lista de números separados por comas: ")
numeros_list = lista.split(",")
numeros = [float(numero) for numero in numeros_list]
media = sum(numeros) / len(numeros)
import math
varianza = sum((x - media) ** 2 for x in numeros) / (len(numeros) - 1)
desviacion_estandar = math.sqrt(varianza)
print(f"\nLa media es: {media}")
print(f"La desviación estándar es: {desviacion_estandar}")
