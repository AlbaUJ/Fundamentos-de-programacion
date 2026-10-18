'''
Ejercicio 3

Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por
comas

'''

numero = int(input("dime un numero entero positivo: "))
texto = ""


for i in  range (1, numero + 1, 2):
    texto = texto + str(i) + ","  

print(texto)

#str(i) convierte en texto, texto = ... añade el numero y una coma