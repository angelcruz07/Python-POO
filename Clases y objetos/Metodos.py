class Celular:
#   Funcion Constructor
   def __init__(self, marca, modelo, camara):
      self.marca = marca
      self.modelo = modelo
      self.camara = camara
# Metodos
   def llamar(self):
      print(f'Llamando desde un: {self.modelo}')
   
   def cortar(self):
      print(f'Cortando llamada desde un: {self.modelo}')

# Propiedades de instancia
celular1 = Celular("Apple", "Iphone 11", "12MP")
print(celular1.llamar())
print(celular1.cortar())
