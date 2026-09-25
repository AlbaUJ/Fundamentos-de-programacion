# Ejercicio 9

#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión.
#(calcular interes compuesto)

cantidad = float(input("dime la cantidad a invertir: "))
interes = float(input("dime el interés anual: "))
años = float(input("dime el numero de años: "))

resultado = round(cantidad * (1 + interes / 100) ** años , 2)

print(f"el capital obtenido es {resultado}")