#Escribir un programa que almacene las matrices:
# A= 1 2 3      B= -1 0
#    4 5 6          0 1
#                   1 1
#en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas, 
#representando cada vector fila en una lista.

A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [-1, 0],
    [0, 1],
    [1, 1]
]
C = [
    [0, 0],
    [0, 0]
]
for i in range(len(A)):          
    for j in range(len(B[0])):   
        for k in range(len(B)):  
            C[i][j] += A[i][k] * B[k][j]
print("El resultado es:")
for fila in C:
    print(fila)
    