'''
Ejercicio 7

Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.

'''

# print (“hola”, end=””) 


for i in range (1, 11): #crea el rango  
    print('\n'"Tabla del", i ,":") # '\n' para que cuando acabe de una tabla haga salto de pagina 
    for j in range (1, 11):
        print(i * j, end=", " )


      
        
    
    
'''
FORMA BÁSICA 
 
for i in range (1,11): ->  crea el rango de tablas del 1 al 10 (la tabla en la que estamos)
    for j in range (1,11):  -> bucle numero 2 por el que se multiplica ej:tabla1: ...x1, ...x2, ...x3
        print (i*j) -> muestra el resultado de la multiplicacion dejando salto de pag despues de cada numero
'''