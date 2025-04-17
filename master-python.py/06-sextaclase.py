"""CALCULADORA DE SUMA, RESTA, MULTIPLICACION Y DIVISON"""

# Bienvenida
print("Bienvenido/a a la calculadora")

# Lista de operaciones a realizar
print("Las operaciones a realizar son: ")
print("1-Suma")
print("2-Resta")
print("3-Multiplicación")
print("4-División")
print("5-Residuo")
print("6-Potenciación")
print("7-Salir de la calculadora")

# Funcion Suma
def suma(numero1, numero2):
    return numero1 + numero2

# Funcion Resta
def resta(numero1, numero2):
    return numero1 - numero2

# Funcion Multiplicacion
def multiplicacion(numero1, numero2):
    return numero1 * numero2

# Funcion Divison
def division(numero1, numero2):
    return numero1 / numero2

# Funcion Residuo
def residuo(numero1, numero2):
    return numero1 % numero2

# Funcion Potenciacion
def potenciacion(numero1, numero2):
    return numero1 ** numero2

operador = None

while True:
    # Operador Suma
    operador = int(input("Ingrese por favor un operador: \n"))
    if operador == 1:
        print("Ha escogido el operador: Suma")
        numero1 = float(input("Ingrese el primer operando\n "))
        numero2 = float(input("Ingrese el segundo operando\n "))
        suma(numero1, numero2)
        rsuma = numero1 + numero2
        print(f"El resultado de la suma sería {rsuma}")
# Operador Resta
    elif operador == 2:
        print("Ha escogido el operador: Resta")
        numero1 = float(input("Ingrese el primer operando\n "))
        numero2 = float(input("Ingrese el segundo operando\n "))
        resta(numero1, numero2)
        rresta = numero1 - numero2
        print(f"El resultado de la resta sería {rresta}")
# Operador Multiplicación
    elif operador == 3:
        print("Ha escogido el operador: Multiplicación")
        numero1 = float(input("Ingrese el primer operando\n "))
        numero2 = float(input("Ingrese el segundo operando\n "))
        multiplicacion(numero1, numero2)
        rmultiplicacion = numero1 * numero2
        print(f"El resultado de la multiplicación sería {rmultiplicacion}")
# Operador División
    elif operador == 4:
        print("Ha escogido el operador: División")
        numero1 = float(input("Ingrese el primer operando\n "))
        numero2 = float(input("Ingrese el segundo operando\n "))
        division(numero1, numero2)
        rdivision = numero1 / numero2
        print(f"El resultado de la división sería {rdivision}")
# Operador Residuo
    elif operador == 5:
        print("Ha escogido el operador: Residuo")
        numero1 = float(input("Ingrese el primer operando\n "))
        numero2 = float(input("Ingrese el segundo operando\n "))
        residuo(numero1, numero2)
        rresiduo = numero1 % numero2
        print(f"El resultado del residuo sería {rresiduo}")
# Operador Potenciación
    elif operador == 6:
        print("Ha escogido el operador: Potenciación")
        numero1 = float(input("Ingrese el primer operando\n "))
        numero2 = float(input("Ingrese el segundo operando\n "))
        potenciacion(numero1, numero2)
        rpotenciacion = numero1 ** numero2
        print(f"El resultado de la potenciacion sería {rpotenciacion}")
    elif operador = 7:
        print("Saliendo de la calculadora")
    else:
        print("Ha escogido una ópcion que no se encuentra en la lista")
        break
