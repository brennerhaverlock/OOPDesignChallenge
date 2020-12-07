from auto import Auto
class Gas(Auto):
    def __init__(self,balance = 100000, wheels = 4, engine = "Gas", model = "Ford Pinto"):
        self.balance = balance
        self.wheels = wheels
        self.engine = engine
        self.model = model

    def setEngine(self):
        """setting engine type to gas"""
        self.engine = "Gas"
        print("You've chosen a gas powered car")