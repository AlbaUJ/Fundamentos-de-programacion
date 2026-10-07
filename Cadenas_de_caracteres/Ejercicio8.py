'''
Ejercicio 8

Escribir un programa que pregunte por consola el precio de un producto en euros
con dos decimales y muestre por pantalla el número de euros y el número de
céntimos del precio introducido


'''

precio = float(input("Dime el precio de un producto en euros y con dos decimales: "))
precio = round(precio,2)
lista = str(precio).split(".") # se pone str porque split solo funciona con texto

print (f"Son {lista[0]} euros y {lista[1]} centimos")