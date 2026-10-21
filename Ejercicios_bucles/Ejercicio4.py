'''
Ejercicio 4

Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas.

'''

numero = int(input("dime un numero entero positivo: "))
texto = ""

for i in  range (numero, -1, -1):  # 1º llega hasta el 0, 2º resta uno en cada vuelta
    texto = texto + str(i) + ","   # convierte i a string y añade una coma despues de cada numero

print(texto)

