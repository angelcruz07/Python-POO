class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print(f'El estudiante {self.nombre} esta estudiando')


nombre = input("Ingresa el nombre del estudiate: ")
edad = input("Cual es la edad del estudiante:")
grado = input("En que grado esta el estudiante: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
  DATOS DEL ESTUDIANTE: 
    Nombre: {estudiante.nombre}

    Edad: {estudiante.edad}

    Grado: {estudiante.grado}
      
    """)


while True:
    estudiar = input()
    if estudiar.lower() == "estudiar":
        estudiante.estudiar()
        break