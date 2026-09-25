# Ejercicio 12

#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
#un descuento del 60%. Escribir un programa que comience leyendo el número de
#barras vendidas que no son del día. Después el programa debe mostrar el precio
#habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
#coste final total.

vendidas = int(input("Dime el número de pan vendido que no son del dia: "))

precio = 3.49
descuento = 0.6

precio_descuento = round(precio * (1-0.6), 2) # 1-0.6 para que de el precio que pagas, no el dinero que te descuentan
coste_total = round(vendidas * precio_descuento, 2)

print (f"El precio habitual de una barra de pan es de {precio}, el descuento por no ser del dia es de {descuento} por lo que el precio a pagar por el pan es de {coste_total} ")