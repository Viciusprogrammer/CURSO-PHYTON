"""COMANDO PARA CALCULAR AlICUOTA INEA A BUQUES DE BANDERA INTERNACIONAL EN VENEZUELA"""

# Gross tonnage o arqueo bruto de un buque
grt = float(input("Ingrese por favor el GRT "))
# Rate of exchange o tasa de cambio
roe = float(input("Ingrese por favor el ROE "))
# Unidad tributaria en Venezuela, última vez actualizada el 13/05/2023
ut = int(9)
constante = float(5.845904058346960)

if grt > 40000:
    print(round(grt*float(0.003*ut*constante*roe), 2))
elif grt >= 20001:
    print(round(grt*float(0.0035*ut*constante*roe), 2))
elif grt >= 5001:
    print(round(grt*float(0.004*ut*constante*roe), 2))
elif grt >= 501:
    print(round(grt*float(0.0045*ut*constante*roe), 2))
elif grt > 0:
    print(round(grt*float(0.01*ut*constante*roe), 2))

print("Gracias por ejecutar nuestro comando")
