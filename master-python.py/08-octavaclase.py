#Importacion de tkinter
from tkinter import *

#Creacion de la ventana principal
root = Tk()

#Evento para el boton
def pulsar_boton():
    Label(root, text="Boton Pulsado.").pack()

#Boton
Button(root, text="¡Púlsame!", command=pulsar_boton).pack()

#Tamaño de la ventana
root.geometry("800x600")

#Titulo de la ventana
root.title("MI PRIMER PROGRAMA")

#Creacion de la etiqueta
mensaje =  Label(root, text="TE AMO RICKY")
mensaje1 = Label(root, text="SIEMPRE")
mensaje2 = Label(root, text="JEJEJE")

#Muestra la etiqueta
#mensaje.grid(row=0, column=0)
#mensaje1.grid(row=0,column=1) 
#mensaje2.grid(row=0,column=2) 

#Bucle de ejecucion
root.mainloop()