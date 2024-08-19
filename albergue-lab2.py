"""
Diseñar un ejercicio que aplique los principios de la Programación
Orientada a Objetos (POO), con su respectiva implementación e
instanciación. El ejercicio debe permitir la entrada de datos por
teclado. Además, proporciona una explicación detallada sobre qué
hace el programa y qué problema resuelve, basado en una situación
problemática de tu entorno.
..............................................................

Una ONG desea brindarle ayuda a familias de escasos recursos en una comunidad
que está siendo afectada por las fuertes lluvias en la zona. Se le preguntará
a un representante de la famila los datos necesarios y si su casa ha sido destruida
se le llevará a un albergue.

CARLOS EDUARDO GARCÍA CASTILLO SMSS045523

"""
class ayuda:
    indice = 0
    def __init__(self,nombre, edad, numFam, trabajo, ingresos, casa  ):
        self.nombre = nombre
        self.edad = edad
        self.numFam = numFam
        self.trabajo = trabajo
        self.ingresos = ingresos
        ayuda.indice += 1
        self.indice = ayuda.indice
        self.casa = casa
        if self.casa == "NO":
            self.casa = "Albergue"
        else:
            self.casa = "Propia"
    

    def mostrarDatos(self):
        print(f"Datos del hogar N {self.indice}\n"+
            f"Nombre: {self.nombre}\n"+
            f"Edad: {self.edad}\n"+
            f"Número de integrantes: {self.numFam}\n"+
            f"Trabajo: {self.trabajo}\n"+
            f"Ingresos: ${self.ingresos}\n"+
            f"Tipo de casa: {self.casa}\n"
            "...................................................."
            )
        
def RecibirDatos():
    num = int(input("¿Cuantos datos quiere registrar?"))
    ayudaHumanitaria = []
    for i in range(num):
        print(".......................................................\n")
        nm = input(f"Nombre del representante: ")
        ed = input("Edad: ")
        numI = input("Número de integrantes: ")
        Trab = input ("Digite su trabajo: ")
        ing = input("Digite sus ingresos: ")
        casaType = input("¿Tiene casa propia? SI/NO: ").upper()
        datos = ayuda(nm,ed,numI,Trab,ing,casaType)
        ayudaHumanitaria.append(datos)
    return ayudaHumanitaria


def MostrarDatos(base):
    print("....................................................\n"+
      "DATOS\n"+
      "....................................................\n")
    for individuo in base:
        individuo.mostrarDatos()


ayudaH = RecibirDatos()
MostrarDatos(ayudaH)