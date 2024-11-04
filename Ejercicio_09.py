#Escribir un programa que pida al usuario una palabra y muestre por pantalla 
#el número de veces que contiene cada vocal.

palabra = input("Introduzca una palabra")
vocales = ["a", "e", "i", "o", "u"]
for i in vocales:
    print (i, "aparece", palabra.count(i), "veces")
    