'''
Ejercicio 2

Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable sin
tener en cuenta mayúsculas y minúsculas.

'''
contraseña = "ConTra123"

pregunta = input("dime la contraseña: ")

if pregunta.lower() == contraseña.lower():  #convertimos ambas a minuscula para que sean iguales
    print("la contraseña es correcta")
else: 
    print("la contraseña no es correcta")