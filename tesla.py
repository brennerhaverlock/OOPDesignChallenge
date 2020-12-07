from auto import Auto
from electric import Electric
from gas import Gas

class Tesla(Electric):
    def __init__(self,price, wheels, engine, model):
        self.price = 80000
        self.wheels = 4
        self.engine = "Electric"
        self.model = "Hummer EV"