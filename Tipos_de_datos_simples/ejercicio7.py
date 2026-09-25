# Ejercicio 7

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
# pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el
# índice de masa corporal calculado redondeado con dos decimales.
 

peso = float(input("dime tu peso en kg: "))
estatura = float(input("dime tu estatura en m: "))

imc = round(peso / (estatura ** 2), 2)

print(f"Tu índice de masa corporal es {imc}")