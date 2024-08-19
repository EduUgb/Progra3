"""
Un concesionario de autos vende vehículos nacionales e importados.
Todos tienen 4 ruedas y capacidad para 5 pasajeros.
Esta informacion debe registrarse siempre por razones de leyes.
Requiere un programa que le permite almacenar las 10 principales 
caracteristicas de los autos. El precio de venta de cada auto es igual
al precio de compra multiplicado por 1.4 que corresponde a su margen de
ganancia.
CARLOS EDUARDO GARCIA CASTILLOS SMSS045523
"""


class auto:
    def __init__(self, marca, modelo, anio, color, tipoMotor, 
                 tipoCombustible, transmision, precioCompra, paisOrigen, kilometraje, placa):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.tipoMotor = tipoMotor
        self.tipoCombustible = tipoCombustible
        self.transmision = transmision
        self.precioCompra = float(precioCompra)
        self.paisOrigen = paisOrigen
        self.kilometraje = kilometraje
        self.placa = placa.upper()
        self.precioVenta = self.Venta()
        self.ruedas = 4
        self.pasajeros = 5



    def Venta(self):
        return self.precioCompra *1.4
        
    def salidaAutos(self):
        print("....................................................\n"+
              f"Datos del auto: \n"+
              "....................................................\n"+
              f"Marca: {self.marca}\n"+
              f"Modelo: {self.modelo}\n"+
              f"Año: {self.anio}\n"+
              f"Color: {self.color}\n"+
              f"Tipo de motor: {self.tipoMotor}\n"+
              f"Tipo de combustible: {self.tipoCombustible}\n"+
              f"Transmisión: {self.transmision}\n"+
              f"Pais de origen: {self.paisOrigen}\n"+
              f"Kilometraje: {self.kilometraje} KM\n"+
              f"Placa: {self.placa}\n"+
              f"Numero de ruedas: {self.ruedas}\n"+
              f"Numero de pasajeros: {self.pasajeros}\n"+
              f"Precio de Compra: {self.precioCompra}\n"+
              f"Precio de Venta: {self.precioVenta:.2f}\n"+
              "....................................................\n")
    
def insDatos():
    marca2 = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    anio = input("Ingrese el año del auto: ")
    color = input("Ingrese el color del auto: ")
    motor = input("Ingrese el tipo de motor del auto: ")
    combustible = input("Ingrese el tipo de combustible del auto: ")
    transmision =input("Ingrese el tipo de transmisión del auto: ")
    pais = input("Ingrese el país de origen del auto: ")
    km = input("Ingrese el kilometraje del auto: ")
    placa = input("Ingrese el número de placa del auto: ")
    precio = input("Ingrese el precio de compra del auto: ")
    return auto(marca2,modelo,anio,color,motor,combustible,transmision,precio,
                pais,km,placa) 


autos = insDatos()
autos.Venta()
autos.salidaAutos()