'''
Ejercicio 10

Escribir un programa que pregunte por consola por los productos de una cesta de la
compra, separados por comas, y muestre por pantalla cada uno de los productos en
una línea distinta

'''


compra = input("Dime productos de la cesta de la compra separados por comas: ")

lista = compra.split(",") # divide por las comas

espacios = compra.replace(',','\n') # reemplaza las comas por espacios

print(espacios)