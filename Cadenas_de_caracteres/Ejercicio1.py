'''
Ejercicio 1

Escribir un programa que pregunte el nombre del usuario en la consola y un número
entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
como el número introducido

'''

nombre = str(input("Dime el nombre del usuario: "))
numero = int(input("Dime un numero entero: "))

print (f"{nombre} \n" * numero)  