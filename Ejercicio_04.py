#Escribir un programa que pregunte al usuario los números ganadores de la 
#lotería primitiva, los almacene en una lista y los muestre por pantalla
#ordenados de menor a mayor.

numeros_ganadores = []
print("Introduzca los números ganadores de la lotería primitiva:")

for i in range(8):
    numero = int(input(f"Número {i + 1}: "))
    numeros_ganadores.append(numero)
numeros_ganadores.sort()
print("\nLos números ganadores son:")
for numero in numeros_ganadores:
    print(numero)

