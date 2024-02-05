class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_description(self):
       return (f"""
    FICHA TECNICA DEL CARRO:

        Marca: {self.brand}
        
        Modelo: {self.model}
        
        Año: {self.year}
    """)
    
    def need_verification(self):
        if int(self.year) < 2015:
            return (f"El carro {self.brand} {self.model} necesita verificación")



brand = input("Ingresa la marca del carro: ")
model = input("Ingresa el modelo del carro: ")
year = input("Ingresa el año del carro: ")


car = Car(brand, model,  year)

print(car.get_description(), car.need_verification())

