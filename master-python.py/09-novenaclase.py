class Motocicleta():
    
    # Atributo de clase
    condicion: "nueva"
    motor: False

    # Métodos
    def __init__(self,color,matricula,combustible_litros,numero_ruedas,marca,modelo,fecha_fabricacion,velocidad_punta,peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.motor = False

    def arrancar(self):
        if self.motor:
            print ("El vehiculo ya se encuentra encendido")
        else:
            print ("Se ha encendido el motor")

    def detener(self):
        if self.motor:
            print ("Se ha detenido el motor")
        else:
            print ("El motor se encuentra apagado")
    
    def consulta_precio(self):
        print (f"El precio de la motocicleta modelo: {self.marca} {self.modelo} es de USD: {self.precio}")

motocicleta_yamaha_1 = Motocicleta("Roja","DBM614",10,2,"YAMAHA","XR1","10/06/2022",300,200)

motocicleta_harley_1 = Motocicleta(

    marca = "HARLEY",
    modelo = "ZH1",
    fecha_fabricacion = "12/04/2022",
    velocidad_punta = 350,
    peso = 190,
    color = "rojo",
    matricula = "YG6Z",
    combustible_litros = 0,
    numero_ruedas = 2,
    )

motocicleta_yamaha_1.precio = 5000
motocicleta_harley_1.precio = 8000

motocicleta_harley_1.consulta_precio()
motocicleta_yamaha_1.consulta_precio()