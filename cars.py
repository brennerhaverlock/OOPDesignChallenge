from auto import Auto
from electric import Electric
from gas import Gas

class Truck(Auto, Electric):
    def __init__(self,price, wheels, engine, model):
        self.price = 80000
        self.wheels = 4
        self.engine = "Electric"
        self.model = "Hummer EV"


class SportsCar(Auto,Gas):
    def __init__(self, price, wheels, engine, model):
        self.price = 100000
        self.wheels = 4 
        self.engine = "Gas"
        self.model = "Corvette 2020"

class SemiTruck(Auto, Gas):
    def __init__(self, price, wheels, engine, model):
        self.price = 110000
        self.wheels = 18 
        self.engine = "Gas"
        self.model = "Big Mac Truck"

