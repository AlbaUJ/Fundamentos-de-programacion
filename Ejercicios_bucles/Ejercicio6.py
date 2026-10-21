'''
Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****

'''

numero = int(input("Dime un numero entero: "))


for i in range (1, numero+1): # recorre secuencia empezando desde el 0 hasta el numero introducido
    print("*" * i) # multiplica lo que queremos imprimir por lo que vale i