from auto import Auto
class Electric(Auto):

    def __init__(self, cars = 1, balance = 50000, price = 50000, wheels = 4, engine = "Electric", model = "Tesla"):
        self.price = price
        self.balance = balance
        self.cars = cars
        self.wheels = 4
        self.engine = engine
        self.model = model


    def set_price(self, price):
        """Set price for any electric car object"""
        self.price = price



    def sellCar(self, price):
        if self.cars < price:
            print("you have sold the car")


    def start(self):
        print("Car started...Battery on")

    def stop(self):
        print("Engine has been turnedd off")
