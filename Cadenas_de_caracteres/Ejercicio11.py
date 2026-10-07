'''
Ejercicio 11
Escribir un programa que pregunte el nombre el un producto, su precio y un número
de unidades y muestre por pantalla una cadena con el nombre del producto seguido
de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

'''

nombre = input("dime el nombre de un producto: ") 
precio = float(input("dime su precio: "))
unidades = int(input("dime el número de unidades: "))

total = unidades * precio


print(f"El producto: {nombre}, cuesta por unidad {precio:09.2f} euros y son {unidades:03}, por lo que el coste total es de {total:011.2f} € ")

#:08.2f -> 0 rellene con ceros, ocupe en total 9 posiciones (la , cuenta) y 2 sean los decimales, f numero decimal
