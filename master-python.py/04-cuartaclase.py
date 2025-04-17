""""PROGRAMA DE PIZZERIA"""

# Welcome
print("Bienvenido/a a nuestra Pizzeria ")

# Variable Assignment
dinero = float(
    input("Ingrese por favor la cantidad de dinero disponible:\n "))
dineroinicial = dinero
total = 0
pedido = []

# Fixed Cost (Pizzas)
margarita = 15.85
vegetariana = 18.95
charcutera = 20.00
primavera = 19.00

# Fixed Cost (Extra Ingredients)
queso = 1.5
jamon = 2.0
chorizo = 3.0
tocineta = 4.0
maiz = 5.0

# Fixed cost (Drinks)
refresco = 2.0
agua = 1.0
nestea = 1.2

# Menu
print("Es un placer para nostros hacerle llegar nuestro menú: ")
print(f"1-Margarita   - {margarita}$")
print(f"2-Vegetariana - {vegetariana}$")
print(f"3-Charcutera  - {charcutera}$")
print(f"4-Primavera   - {primavera}$")
print("5-No deseo añadir más pizzas")


# Pizza Selection
while True:
    eleccion = int(input("Seleccione una opción: \n "))
    if eleccion == 1:
        print("Ha escogido una pizza tipo: Margarita")
        dinero -= margarita
        total += margarita
        pedido.append(f"Margarita - {margarita}")
        print(f"Hasta los momentos lleva un sub-total de USD {total}")
        print(f"Le van quedando USD {dinero}")
    elif eleccion == 2:
        print("Ha escogido una pizza tipo: Vegetariana")
        dinero -= vegetariana
        total += vegetariana
        pedido.append(f"Vegetariana - {vegetariana}")
        print(f"Hasta los momentos lleva un sub-total de USD {total}")
        print(f"Le van quedando USD {dinero}")
    elif eleccion == 3:
        print("Ha escogido una pizza tipo: Charcutera")
        dinero -= charcutera
        total += charcutera
        pedido.append(f"Charcutera - {charcutera}")
        print(f"Hasta los momentos lleva un sub-total de USD {total}")
        print(f"Le van quedando USD {dinero}")
    elif eleccion == 4:
        print("Ha escogido una pizza tipo: Primavera")
        dinero -= primavera
        total += primavera
        pedido.append(f"Primavera - {primavera}")
        print(f"Hasta los momentos lleva un sub-total de USD {total}")
        print(f"Le van quedando USD {dinero}")
    elif eleccion == 5:
        print("No deseo añadir más pizzas")
        break
    else:
        print("Ha escogido una ópcion no válida de pizza")
        break

# Extra Ingredients Menu
while True:
    print("¿Desea agregar un ingrediente extra a su pizza?")
    print(f"1-Queso    - {queso}$")
    print(f"2-Jamón    - {jamon}$")
    print(f"3-Chorizo  - {chorizo}$")
    print(f"4-Tocineta - {tocineta}$")
    print(f"5-Maiz     - {maiz}$")
    print("6-No deseo añadir / añadir más ingredientes extras")

# Extra Ingredients Selection
    eleccion = int(input("Seleccione una opción: \n "))
    if eleccion == 1:
        print("Ha escogido una extra tipo: Queso")
        total += queso
        dinero -= queso
        pedido.append(f"Queso - {queso}")
        print(f"Le quedan USD {dinero}")
    elif eleccion == 2:
        print("Ha escogido una extra tipo: Jamón")
        total += jamon
        dinero -= jamon
        pedido.append(f"Jamón - {jamon}")
        print(f"Le quedan USD {dinero}")
    elif eleccion == 3:
        print("Ha escogido una extra tipo: Chorizo")
        total += chorizo
        dinero -= chorizo
        pedido.append(f"Chorizo - {chorizo}")
        print(f"Le quedan USD {dinero}")
    elif eleccion == 4:
        print("Ha escogido una extra tipo: Tocineta")
        total += tocineta
        dinero -= tocineta
        pedido.append(f"Tocineta - {tocineta}")
        print(f"Le quedan USD {dinero}")
    elif eleccion == 5:
        print("Ha escogido una extra tipo: Maíz")
        total += maiz
        dinero -= maiz
        pedido.append(f"Maíz - {maiz}")
        print(f"Le quedan USD {dinero}")
    elif eleccion == 6:
        print("Perfecto, no desea añadir ingredientes extra")
        break
# Drinks Menu
while True:
    print("¿Desea agregar una bebida a su pedido?")
    print(f"1-Agua     - {agua}$")
    print(f"2-Nestea   - {nestea}$")
    print(f"3-Refresco - {refresco}$")
    print("4-No deseo añadir más bedidas")

# Drinks Selection
    eleccion = int(input("Seleccione una opción: \n "))
    if eleccion == 1:
        print("Ha escogido una bebida tipo: Agua")
        total += agua
        dinero -= agua
        pedido.append(f"Agua - {agua}")
        print(f"Le quedan USD {dinero}")
    elif eleccion == 2:
        print("Ha escogido una bebida tipo: Nestea")
        total += nestea
        dinero -= nestea
        pedido.append(f"Nestea - {nestea}")
        print(f"Le quedan USD {dinero}")
    elif eleccion == 3:
        print("Ha escogido una bebida tipo: Refresco")
        total += refresco
        dinero -= refresco
        pedido.append(f"Refresco - {refresco}")
        print(f"Le quedan USD {dinero}")
    else:
        print("No deseo añadir más bedidas")
        break

# Formula to print (or not), if the initial money is bigger than total amount
if total <= dineroinicial:
    print(f"----Su orden es la siguiente---- \n {pedido}")
    vuelto = (round(dineroinicial - total, 2))
    print(f"Su vuelto sería: USD {vuelto}")
else:
    print("No alcanza el dinero introducido, por favor recargue")
