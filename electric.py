from auto import Auto
class Electric():

    def __init__(self):
        super().__init__(100000, 4, "Electric", 150)

    balance = 100000
    cars = 0
    #The setWheels and setEngine are also inherited 

    def start(self):
        print("Car started...Battery on")

    def stop(self):
        print("Engine has been turnedd off")
