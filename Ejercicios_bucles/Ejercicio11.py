'''
Ejercicio 11

Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
una a una las letras de la palabra introducida empezando por la última

'''


frase = input("dime una frase: ")
letra = input("dime una letra: ")


for letra in frase[::-1]: #invertir palabra
    print(letra) #cada letra en una linea diferente 