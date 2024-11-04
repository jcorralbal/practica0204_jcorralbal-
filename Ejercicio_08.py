#Escribir un programa que pida al usuario una palabra y muestre por pantalla 
#si es un palíndromo.


palabra = input("Introduzca una palabra: ")
palabra_verif = palabra.replace(" ", "").lower()
if palabra_verif == palabra_verif[::-1]:
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")
    