'''
Ejercicio 3

Escribir un programa que pregunte el nombre del usuario en la consola y después
de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n>
letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el
número de letras que tienen el nombre

'''

nombre = input("Dime el nombre del usuario: ")
n = len(nombre.replace(" ", ""))

print (f"El nombre {nombre} tiene {n} letras, donde {nombre.upper()}  es el nombre de usuario en mayúsculas y {n} es el numero de letras que tiene el nombre")