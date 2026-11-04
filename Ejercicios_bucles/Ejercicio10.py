'''
Ejercicio 10

Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no.

'''

numero = int(input("dime un numero entero: "))



for i in range (2,numero): # comprueba del 2 al numero-1
    if numero % i == 0: 
        print(f"El numero {numero} no es primo")
        break
else:
    print(f"El numero {numero} es primo")

# solo es primo si solo da 0 al dividirlo con 1 y él mismo


# con el for no comprueba ni el 1 no el numero introducido porque todos son divisibles
# por 1 y por si mismo, si encuentra un numero desde el 2 hasta numero-1 que de resto
# de 0 ya no seria primo porque solo son primos los que dan 0 solo entre 1 y si mismo
# 
# 
# 
# EJEMPLO: 
# numero = 7 
# comprueba desde el 2 hasta el 6 -> como ninguno de esos da de resultado 0, es primo 
