#Escribir un programa que almacene en una lista los números del 1 al 10 y los
#muestre por pantalla en orden inverso separados por comas.

numeros = list(range(1, 11))
numeros_inv = numeros[::-1]
result_numeros = [str(numero) for numero in numeros_inv]
resultado = ', '.join(result_numeros)
print(resultado)
