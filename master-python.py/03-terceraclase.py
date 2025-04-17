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

operador = None
operador = int(input("Ingrese por favor un operador: \n"))
if operador == 1:
    print("Ha escogido el operador: Suma")
    s1 = float(input("Ingrese el primer operando\n "))
    s2 = float(input("Ingrese el segundo operando\n "))
    print(round((s1+s2), 2))
# Operador Resta
elif operador == 2:
    print("Ha escogido el operador: Resta")
    r1 = float(input("Ingrese el primer operando\n "))
    r2 = float(input("Ingrese el segundo operando\n "))
    print(round((r1-r2), 2))
# Operador Multiplicación
elif operador == 3:
    print("Ha escogido el operador: Multiplicación")
    m1 = float(input("Ingrese el primer operando\n "))
    m2 = float(input("Ingrese el segundo operando\n "))
    print(round((m1*m2), 2))
# Operador División
elif operador == 4:
    print("Ha escogido el operador: División")
    d1 = float(input("Ingrese el primer operando\n "))
    d2 = float(input("Ingrese el segundo operando\n "))
    print(round((d1/d2), 2))
# Operador Residuo
elif operador == 5:
    print("Ha escogido el operador: Residuo")
    re1 = float(input("Ingrese el primer operando\n "))
    re2 = float(input("Ingrese el segundo operando\n "))
    print(round((re1 % re2), 2))
# Operador Potenciación
elif operador == 6:
    print("Ha escogido el operador: Potenciación")
    p1 = float(input("Ingrese el primer operando\n "))
    p2 = float(input("Ingrese el segundo operando\n "))
    print(round((p1**p2), 2))
else:
    print("Ha escogido una ópcion que no se encuentra en la lista")
    print("Por favor, corra nuevamente la calculadora.")
