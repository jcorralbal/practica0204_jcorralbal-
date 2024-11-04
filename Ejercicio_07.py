#Escribir un programa que almacene el abecedario en una lista, elimine de la 
#lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla
#la lista resultante.

abecedario = list('abcdefghijklmnopqrstuvwxyz')
print("Abecedario:")
print(abecedario)
abecedario_filtrado = [letra for idx, letra in enumerate(abecedario, start=1) if idx % 3 != 0]
print("\nAbecedario nuevo:")
print(abecedario_filtrado)
