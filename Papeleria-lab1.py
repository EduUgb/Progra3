"""
Una papeleria vende cuadernos y lapices. Los cuadernos pueden ser de 50 o 100 hojas.
Los lapices pueden ser de grafito o de colores. El precio de veenta es igual al  
precio al precio de compra multiplicado por 1.30 que corresponde al margen
de ganancia. La papeleria requiere construir un programa que le permite registrar
y visualizar por lo menos dos articulos de item. Todos los cuadernos son marca HOJITAS
y los lapices son marca RAYITAS aya que la papeleria es un distribuidor exclusivo
"""
class Cuaderno:

    indice = 0

    def __init__(self, hojas, precioCompra ):
        self.marca = "HOJITAS"
        self.hojas = int(hojas)
        self.precioCompra = float(precioCompra) 
        self.precioVenta =  self.CalculopVenta()
        Cuaderno.indice += 1
        self.indice = Cuaderno.indice
    

    def CalculopVenta(self):
       return self.precioCompra * 1.30

    def salidaCuadernos(self):
        print(f"Cuaderno N{self.indice}:\n"+
            f"Marca: {self.marca}\n"+
            f"Numero de hojas: {self.hojas}\n"+
            f"Precio de compra: ${self.precioCompra:.2f}\n"+
            f"Precio de venta: ${self.precioVenta:.2f}\n"
            )

"......................................................."


class Lapiz:
    indice = 0
    def __init__(self, tipo, precioCompra ):
        self.marca = "RAYITAS"
        self.tipo = str(tipo)
        self.precioCompra = float(precioCompra) 
        self.precioVenta =  self.CalculopVenta()
        Lapiz.indice += 1
        self.indice = Lapiz.indice

    def CalculopVenta(self):
       return self.precioCompra * 1.30


    def salidaLapices(self):
        print(f"Lapiz N{self.indice}:\n"+
            f"Marca: {self.marca}\n"+
            f"Tipo de lapiz: {self.tipo}\n"+
            f"Precio de compra: ${self.precioCompra:.2f}\n"+
            f"Precio de venta: ${self.precioVenta:.2f}\n"+
            "....................................................\n"
            )

"......................................................"

def RecDatos1():
    cuadernoLista = []
    numero = int(input("¿Cuantos cuadernos quiere registrar?: "))
    for i in range(numero):
        numh = int(input(f"Ingrese las hojas del cuaderno {i+1} (50/100): "))
        prCompra = float(input("Precio de compra: "))
        cuaderno = Cuaderno(numh,prCompra)
        cuadernoLista.append(cuaderno)
    return cuadernoLista

       
def RecDatos2():
    lapicesLista = []
    numero = int(input("¿Cuantos lapices quiere registrar?: "))
    for i in range(numero):
        tipo = input(f"Ingrese el tipo del lapiz {i+1} (grafito/colores): ")
        prCompra = input("Precio de compra: ")
        lapices = Lapiz(tipo,prCompra)
        lapicesLista.append(lapices)
    return lapicesLista


def MostrarDatos(ListaC,ListaL):
    print(".......................................................\nCUADERNOS\n"+
        ".......................................................")
        
    for dato in ListaC:
        dato.salidaCuadernos()
    print(".......................................................\nLapices\n"+
        ".......................................................")
    
    for dato in ListaL:
        dato.salidaLapices()



datosCuaderno=RecDatos1()
datosLapiz=RecDatos2()
print(".......................................................\nDATOS:")
MostrarDatos(datosCuaderno,datosLapiz)
