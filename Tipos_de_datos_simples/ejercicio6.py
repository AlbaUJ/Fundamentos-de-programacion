
# Ejercicio 6

#Escribir un programa que lea un entero positivo, , introducido por el usuario y
#después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La
#suma de los primeros enteros positivos puede ser calculada de la siguiente forma

n = int(input("Dime un numero entero positivo: "))
suma = n * (n+1) //2

if n < 0 : 
    print("tiene que ser un numero positivo")
else:
    print (suma)
