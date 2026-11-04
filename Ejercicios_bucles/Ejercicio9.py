'''
Ejercicio 9

Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
correcta.

'''


contraseña = "contra123"

pregunta = input("Introduce la contraseña: ")

while pregunta != contraseña:  # mientras no sea correcta sigue preguntando
    print ("Contraseña incorrecta")
    print()
    pregunta = input("introduce la contraseña: ")
print("La contraseña es correcta")  # si la contraseña es correcta y sale del bucle muestra el print