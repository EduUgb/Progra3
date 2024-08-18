"""
Una veternaria atiende solamente perros y los registra
en una base de datos. Se requiere un programa que lea la informacion 
basica de un perro (no mas de 8 caracteristicas) y se muestre en pantalla.
En esta veterinaria todos los animales que llegan, entran en el estado inicial
de NO ATENDIDO y cuando se registran se cambia automaticamente a ATENDIDO. Por
ahora como  la veterinaria solo atiende perros, basado en el peso (menos de 10kg
o mas de 10kg) los registra como "Perro grande" o "Perro pequeño"
"""

class Perro:

    indice = 0
    def __init__(self,nombre, edad, raza, vacunado, peso, color, duenio):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.vacunado = vacunado.upper()
        self.peso = float(peso)
        self.color = color
        self.duenio = duenio
        Perro.indice += 1
        self.indice = Perro.indice
        self.estado =   "NO ATENDIDO"
        if self.peso > 10:
           self.tamanio = "Perro grande"
        else:
           self.tamanio= "Perro pequeño"


    def registra(self):
       self.estado="ATENDIDO"

    def mostrarDatos(self):
        print(f"Datos del perro N {self.indice}\n"+
            f"Nombre: {self.nombre}\n"+
            f"Edad: {self.edad}\n"+
            f"Raza: {self.raza}\n"+
            f"Vacunas: {self.vacunado}\n"+
            f"Peso: {self.peso} kg\n"+
            f"Color: {self.color}\n"
            f"Tamaño: {self.tamanio}\n"
            f"Estado: {self.estado}\n"
            f"Dueño: {self.duenio}\n"
            "...................................................."
            )

def RecDatos():
    num = int(input("¿Cuantos perros quiere registrar?"))
    baseDeDatos = []
    for i in range(num):
        print(".......................................................\n")
        nm = input(f"Nombre del perro {i+1}: ")
        ed = input("Edad: ")
        ra = input("Raza: ")
        va = input ("Está vacunado? SI/NO: ")
        pe = input("Peso (KG): ")
        col = input("Color del pelaje: ")
        du = input("Nombre del dueño: ")
        perros = Perro(nm,ed,ra,va,pe,col,du)
        baseDeDatos.append(perros)
    return baseDeDatos

def MostrarDatos(base):
    print("....................................................\n"+
      "DATOS\n"+
      "....................................................\n")

    for dato in base:
        dato.registra()
        dato.mostrarDatos()



datosperro=RecDatos()
MostrarDatos(datosperro)



