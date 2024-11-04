#Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al 
#usuario la nota que ha sacado en cada asignatura y elimine de la lista las
#asignaturas aprobadas. Al final el programa debe mostrar por pantalla las 
#asignaturas que el usuario tiene que repetir.

notas = [] 
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

for i in range(len(asignaturas)):
    nota = float(input("Nota en " + asignaturas[i] + ": "))
    notas.append(nota)

asignaturas_repetir = []
for i in range(len(asignaturas)):
    if notas[i] < 5:
        asignaturas_repetir.append(asignaturas[i])

if asignaturas_repetir:
    print("Tienes que repetir las siguientes asignaturas:")
    for asignatura in asignaturas_repetir:
        print(asignatura)
else:
    print("Has aprobado todas las asignaturas :) ")
    