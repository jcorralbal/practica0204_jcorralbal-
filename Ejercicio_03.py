#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al
#usuario la nota que ha sacado en cada asignatura, y después las muestre por
#pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura>
#es cada una des las asignaturas de la lista y <nota> cada una de las 
#correspondientes notas introducidas por el usuario.

print("Notas de tus asignaturas")

notas = [] 
asignaturas =["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in range(len(asignaturas)):
    notas.append(input("Nota en " + asignaturas[i] + ": "))
for i in range(len(asignaturas)):
    print("En", asignaturas[i], "has sacado", notas[i])

