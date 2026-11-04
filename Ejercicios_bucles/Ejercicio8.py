'''
Ejercicio 8

Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1


'''

numero = int(input("dime un numero entero: "))

for i in range (-1, numero+1, 2 ): # empieza en -1 para que aparezca el 1, numero+1 para que aparezca el que hemos introducido, 2 para que vaya de dos en dos
    for j in range (i, -1, -2): # empieza por i, hasta -1 para que aparezca el 1, -2 para que vaya de dos en dos hacia atrás
        print(j, end=" ") # imprime cada numero desde el 1 hasta el introducido de dos en dos añadiendo en cada vuelta uno 
    print() # para hacer un salto de línea despues de cada fila



# en el segundo for como retrocede 2, la línea empieza en el 3 y asi consecutivamente