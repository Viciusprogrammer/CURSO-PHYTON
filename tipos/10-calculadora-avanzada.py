"""COMANDO PARA REALIZAR UNA CÁLCULADORA AVANZADA"""

print("BIENVENIDOS A NUESTRA CALCULADORA")
print("LOS OPERADORES A TOMAR EN CUENTA SERIAN: SUMA, RESTA, MUTIPLICACION Y DIVISON")
print("A FIN DE CERRAR LA CALCULADORA POR FAVOR ESCBRIBA \"SALIR\"")

resultado = ""
while True:
      if not resultado:
            resultado = input ("Ingrese un número: ")
            if resultado.lower () == "salir":
             break
            resultado = int(resultado)
        op = input("Ingresa operacion: ")
                if op.lower () == "salir":
        break
      