'''
Ejercicio 13

Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
que el usuario escriba “salir” que terminará.

'''

echo = ""

while echo != "salida":
    echo = input("Escribe algo: ") 
    print (echo)
print ("adios") #lo muestra cuando sale del while