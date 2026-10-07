'''
Ejercicio 9

Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
anterior para que también funcione cuando el día o el mes se introduzcan con un
solo carácter

'''

fecha = input("Dime la fecha de tu cumpleaños en formato dd/mm/aaaa: ")
lista = fecha.split('/')

print (f"Naciste el dia {lista[0]} del mes {lista[1]} del año {lista[2]}")