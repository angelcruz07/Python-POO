class Phone:
#   Funcion Constructor
   def __init__(self, brand, model, camera):
      self.brand = brand
      self.model = model
      self.camera = camera
# Methods
   def call(self):
      print(f'Calling from a : {self.model}')
   
   def hang_up(self):
      print(f'Hanging up from a : {self.model}')

# Intance properties
phone = Phone("Apple", "Iphone 11", "12MP")
print(phone.call())
print(phone.hang_up())
