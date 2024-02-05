class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_description(self):
        return f"""
    CAR SPECIFICATIONS:

        Brand: {self.brand}
        
        Model: {self.model}
        
        Year: {self.year}
    """
    
    def need_verification(self):
        if int(self.year) < 2015:
            return f"The car {self.brand} {self.model} needs verification"


brand = input("Enter the car brand: ")
model = input("Enter the car model: ")
year = input("Enter the car year: ")

car = Car(brand, model,  year)

print(car.get_description(), car.need_verification())
