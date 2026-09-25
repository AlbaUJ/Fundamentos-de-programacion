# Ejercicio 11

#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
#interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
#año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que
#comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
#introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
#la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada
#cantidad a dos decimales.

cantidad = float(input("Dime la cantidad depositada:  "))

cantidad =  cantidad * 1.04  # puede ser * 1.04 o cantidad = cantidad + cantidad * 0.04 (1 es el 100% del dinero)
print (f"Los ahorros del primer año son  {round (cantidad,2)}")

cantidad =  cantidad * 1.04
print (f"Los ahorros del segundo año son {round (cantidad,2)}")

cantidad =  cantidad * 1.04
print (f"Los ahorros del tercer año son {round (cantidad,2)}")