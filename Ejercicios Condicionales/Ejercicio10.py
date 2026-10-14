'''
Ejercicio 10

La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.
● Ingredientes vegetarianos: Pimiento y tofu.
● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
en función de su respuesta le muestre un menú con los ingredientes disponibles
para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
pizza elegida es vegetariana o no y todos los ingredientes que lleva

'''

tipo = input("¿Quieres una pizza vegetariana? (si/no): ").lower()


if tipo == "si": 
    print("Ingredientes vegetarianos: pimientos y tofu")
    ingrediente = ["pimientos", "tofu"]
    veget = input("elige solo un ingrediente: ").lower()
    if veget in ingrediente:
          print (f"La pizza es vegetariana, y los ingredientes son: tomate, mozzarella y {veget}")
    else: print ("ingrediente no valido")
elif tipo == "no":
    print ("Ingredientes no vegetarianos: peperoni, jamón y salmón")
    ingrediente = ["peperoni", "jamon", "salmon"]
    noVeget = input("elige solo un ingrediente: ").lower()
    if noVeget in ingrediente:
        print (f"La pizza no es vegetariana, y los ingredientes son: tomate, mozzarella y {noVeget}")
    else: 
        print("ingrediente no valido")
else:
    print ("debes responder si o no ");

