operador = None

# Funcion Suma


def suma(numero1, numero2):
    return numero1 + numero2


resultado1 = suma(10, 45)
resultado2 = suma(67, 45)
sumas_sumas = resultado1 + resultado2
print(sumas_sumas)

# Funcion Resta


def resta(numero1, numero2):
    return numero1 - numero2


resultado1 = resta(45, 45)
resultado2 = resta(67, 375)
resta_restas = resultado1 + resultado2
print(resta_restas)

operador = int(input("Ingrese por favor un operador: \n"))

if operador == 1:
    print("Ha escogido el operador: Suma")
    suma

if operador == 2:
    print("Ha escogido el operador: Suma")
    resta
