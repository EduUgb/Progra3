"""
Un almacen vende dispositivos electronicos(celulares, tablets y portátiles).
Todos PHR que son una nueva marca que está entrando en el mercado.
Se requiere almacenar sus 6 principales características.
Todos son productos importados y su precio de venta es igual al precio de compra multiplicado
por 1.7 que corresponde a su margen de ganancia
"""
class Almacen:
    indice = 0
    def __init__(self, tipo, modelo, color, procesador, pantalla, camara, precioCompra):
        self.tipo = tipo
        self.modelo = modelo
        self.color = color
        self.procesador = procesador
        self.pantalla = pantalla
        self.camara= camara
        self.precioCompra = float(precioCompra)
        self.marca = "PHR"
        Almacen.indice += 1
        self.indice = Almacen.indice
        self.precioVenta = self.venta()

    def venta(self):
        return self.precioCompra * 1.7
    

    def salida(self):
        print("....................................................\n"+
        f"Datos del dispositivo {self.indice}:\n"+
        "....................................................\n"+
        f"Tipo de dispositivo: {self.tipo}\n"+
        f"Marca: {self.marca}\n"+
        f"Modelo: {self.modelo}\n"+
        f"Color: {self.color}\n"+
        f"Procesador: {self.procesador}\n"+
        f"Tipo de pantalla: {self.pantalla}\n"+
        f"Calidad de cámara: {self.tipo} megapixeles\n"+
        f"Precio de Compra: ${self.precioCompra:.2f}\n"+
        f"Precio de Venta: ${self.precioVenta:.2f}\n"+
        "....................................................\n")

    
def ingDatos():
    num = int(input("Cuantos dispositivos desea ingresar?: "))
    dispositivos = []
    for i in range(num):
        print(f".......................................................\nIngrese los datos del dispositivo N{i+1}:")
        tipo = input("Ingrese el tipo de dispositivo (Smartphone/tablet/laptop): ")
        modelo = input("Ingrese el modelo del dispositivo: ")
        color = input("Ingrese el color del dispositivo: ")
        procesador = input("Ingrese el procesador: ")
        pantalla = input("Ingrese el tipo de pantalla: ")
        camara =input("Ingrese la calidad de la cámara (Megapixeles): ")
        precio = input("Ingrese el precio de compra del dispositivo: ")
        dispositivo1 = Almacen(tipo,modelo,color,procesador,pantalla,camara,precio)
        dispositivos.append(dispositivo1)
    return dispositivos

def MostrarDatos(dispositivos):
    for dato in dispositivos:
        dato.salida()

datos = ingDatos()
MostrarDatos(datos)