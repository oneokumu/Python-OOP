class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Details:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}")

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2024)

# Call the display_info() method
my_car.display_info()
