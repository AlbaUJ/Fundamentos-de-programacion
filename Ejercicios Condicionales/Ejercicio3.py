'''
Ejercicio 3

Escribir un programa que pida al usuario dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error.

'''

numero1 = int(input("introduce un numero: "))
numero2 = int(input("introduce otro numero: "))



if numero2 == 0:
    print("ERROR, el divisor no puede ser cero")
else: 
    division = (numero1 / numero2)
    print(division)