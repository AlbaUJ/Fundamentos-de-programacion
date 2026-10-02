'''
Ejercicio 8

Escribir un programa que pregunte por consola el precio de un producto en euros
con dos decimales y muestre por pantalla el número de euros y el número de
céntimos del precio introducido


'''

precio = input("Dime el precio de un producto en euros y con dos decimales: ")
lista = precio.split(".")

print (f"Son {lista[0]} euros y {lista[1]} centimos")