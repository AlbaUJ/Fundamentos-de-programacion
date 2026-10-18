'''
Ejercicio 5

Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
año que dura la inversión.

'''

cantidad = float(input("que cantidad vas a invertir: "))
interes = float(input("con cuanto interés: "))
años = int(input("durante cuantos años: "))

calculo = cantidad # para que la cantidad se pueda incrementar en el bucle

for i in range(1, años + 1 ):
    calculo = calculo + (calculo  * interes)/100
    print(f"{i}º año: {calculo:.2f} €" )